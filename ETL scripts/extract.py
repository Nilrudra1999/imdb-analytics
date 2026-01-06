"""----------------------------------------------------------------------------
    Main Extractor File - Extracts raw data from API to store in CSV
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This script uses the FreeIMDb & OMDb APIs along with the 
    imdb_movie_ids.txt file to extract live movie data. It doesn't change 
    the data but simply places it inside the data/raw/data.csv file.
----------------------------------------------------------------------------"""
import os
import csv
import json
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()
__imdb_url = os.getenv("IMDB_API_BASE_URL")
__omdb_url = os.getenv("OMDB_API_BASE_URL")
__api_key = os.getenv("API_KEY")
__starting_row = int(os.getenv("EXT_STARTING_ROW", 0))
__BASE_DIR = Path(__file__).resolve().parent.parent
__ID_FILE = __BASE_DIR / "data" / "imdb_movie_ids.txt"
__RAW_CSV =__BASE_DIR / "data" / "raw" / "data.csv"
__ENV_FILE = __BASE_DIR / "ETL scripts" / ".env"
__MAX_MOVIES = 10


# APIs only allow 1000 requests daily, but the number of IDs > 1000
# so for leftover IDs from pervious runs __move_to_starting_row() skips over them
def process_movie_data_extraction():
    row_count = 0
    with open(__ID_FILE, "r", encoding="utf-8") as read_file, \
         open(__RAW_CSV, "w", encoding="utf-8") as write_file:
        writer = csv.writer(write_file)
        writer.writerow(["movie_id", "omdb_data", "box_office_data"])
        __move_to_starting_row(read_file)
        
        while row_count < __MAX_MOVIES:
            record = read_file.readline()
            if not record: break # EOF state
            movie_id = record.strip()
            movie_data = __fetch_omdb_data(movie_id)
            movie_bo_data = __fetch_box_office_data(movie_id)
            writer.writerow([
                movie_id, 
                json.dumps(movie_data), 
                json.dumps(movie_bo_data)
            ])
            row_count += 1
        
        __update_starting_row_count(__starting_row + row_count)


def __move_to_starting_row(read_file):
    for _ in range(__starting_row): read_file.readline()


def __update_starting_row_count(value: int):
    lines = __ENV_FILE.read_text().splitlines()
    lines[-1] = f"EXT_STARTING_ROW={value}"
    __ENV_FILE.write_text("\n".join(lines) + "\n")
    print(f"Updated EXT_STARTING_ROW={value} in .env")


def __fetch_omdb_data(movie_id):
    params = {"apikey": __api_key, "i": movie_id}
    response = requests.get(__omdb_url, params=params)
    return response.json()


def __fetch_box_office_data(movie_id):
    url = f"{__imdb_url}{movie_id}/boxOffice"
    response = requests.get(url)
    return response.json()
