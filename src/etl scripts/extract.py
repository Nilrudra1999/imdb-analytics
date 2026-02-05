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
from csv import writer
from json import dumps
from os import getenv
import requests
from dotenv import load_dotenv

load_dotenv()
__IMDB_URL  = getenv("IMDB_API_BASE_URL")
__OMDB_URL  = getenv("OMDB_API_BASE_URL")
__API_KEY   = getenv("API_KEY")

# Free IMDb API has a "at one time" response limit of 50
# The limit restarts after 20-30 mins (hypothetically)
# OMDb API has a total daily limit of 1000 total requests
__ID_CURSOR  = int(getenv("ID_CURSOR", 0))
__MAX_MOVIES = 50


# the "cursor position" being referred to within this method is linked to an env variable
# the variable keeps track of where the ETL pipeline last left off when collecting data
def fetch_movie_data_from_api(base_directory):
    ids_file  = base_directory / "data" / "imdb_movie_ids.txt"
    raw_csv   = base_directory / "data" / "raw" / "data.csv"
    env_file  = base_directory / "src" / "etl scripts" / ".env"
    row_count = 0
    
    reader_file = __open_reader_file(ids_file)
    writer_file = __open_writer_file(raw_csv)
    csv_writer  = writer(writer_file)
    csv_writer.writerow(["movie_id", "omdb_data", "box_office_data"])
    
    __move_to_cursor_position(reader_file)
    row_count = __fetching_data(row_count, reader_file, csv_writer)
    __update_cursor_position(__ID_CURSOR + row_count, env_file)



def __fetching_data(row_count, dataset_read, dataset_write):
    while row_count < __MAX_MOVIES:
        record = dataset_read.readline()
        if not record: # EOF state
            print("Data for all specified IMDb IDs have been acquired")
            break
        
        movie_id = record.strip()
        movie_data = __fetch_omdb_data(movie_id)
        box_office_data = __fetch_box_office_data(movie_id)
        dataset_write.writerow([
            movie_id, 
            dumps(movie_data), 
            dumps(box_office_data)
        ])
        
        row_count += 1
    return row_count



def __fetch_omdb_data(movie_id):
    params = {"apikey": __API_KEY, "i": movie_id}
    try:
        response = requests.get(__OMDB_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"OMDB Error: {e}")
        return {"error": "OMDB fetch failed"}



def __fetch_box_office_data(movie_id):
    url = f"{__IMDB_URL}{movie_id}/boxOffice"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching box office for {movie_id}: {e}")
        return {"error": "Could not retrieve data"}



def __move_to_cursor_position(dataset):
    for _ in range(__ID_CURSOR): dataset.readline()


def __update_cursor_position(value: int, env_file):
    lines = env_file.read_text().splitlines()
    lines[-1] = f"ID_CURSOR={value}"
    env_file.write_text("\n".join(lines) + "\n")
    print(f"ID_CURSOR is at position {value} in .env")


def __open_reader_file(dataset):
    reader_file = open(dataset, "r", encoding="utf-8")
    return reader_file


def __open_writer_file(dataset):
    writer_file = open(dataset, "w", encoding="utf-8")
    return writer_file
