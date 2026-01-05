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
__MAX_MOVIES = 3


# since the APIs only allow 1000 requests daily, the ETL pipeline can only extract that much
# each time the pipeline runs the starting row to read from changes, since num of IDs > 1000
def extract_raw_json_for_csv():
    row_count = 0
    with open(__ID_FILE, "r", encoding="utf-8") as id_file, open(__RAW_CSV, "a", encoding="utf-8") as out_file:
        for _ in range(__starting_row): # discarding (n) lines
            line = id_file.readline()
            if not line:
                print(f"Reached EOF before starting row {__starting_row}")
                return
        
        while row_count < __MAX_MOVIES:
            line = id_file.readline()
            if not line: break # EOF state

            movie_id = line.strip()
            movie_data = __fetch_omdb_data(movie_id)
            movie_BO_data = __fetch_box_office_data(movie_id)

            out_file.write(f"Movie ID: {movie_id}\n")
            out_file.write(f"{movie_data}\n")
            out_file.write(f"{movie_BO_data}\n")
            row_count += 1
        update_starting_row_count_env(__starting_row + row_count)


def update_starting_row_count_env(value: int):
    env_file = __BASE_DIR / "ETL scripts" / ".env"
    lines = env_file.read_text().splitlines()
    lines[-1] = f"EXT_STARTING_ROW={value}"
    env_file.write_text("\n".join(lines) + "\n")
    print(f"Updated EXT_STARTING_ROW={value} in .env")


def __fetch_omdb_data(movie_id):
    params = {"apikey": __api_key, "i": movie_id}
    response = requests.get(__omdb_url, params=params)
    return response.json()


def __fetch_box_office_data(movie_id):
    url = f"{__imdb_url}{movie_id}/boxOffice"
    response = requests.get(url)
    return response.json()
