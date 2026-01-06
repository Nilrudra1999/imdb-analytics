"""----------------------------------------------------------------------------
    Main Transformer File - Transforms raw CSV data to tabular format
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This script uses the data/raw/data.csv and data/processed/data.csv
    files to transform the raw csv data into a more tabular format 
    after cherry picking the necessary information needed for the DB.
----------------------------------------------------------------------------"""
import csv
import json
from pathlib import Path
from datetime import datetime

__BASE_DIR = Path(__file__).resolve().parent.parent
__RAW_CSV = __BASE_DIR / "data" / "raw" / "data.csv"
__PROCESSED_CSV = __BASE_DIR / "data" / "processed" / "data.csv"
__movie_json_fieldnames = [
    "Title", "Runtime", "Released", "Country", 
    "Director", "Writer", "Actors",
    "Genre", "Ratings", "Awards"
]
__box_office_json_fieldnames = [
    "productionBudget", "domesticGross",
    "worldwideGross", "openingWeekendGross"
]


def process_movie_data_transformations():
    with open(__RAW_CSV, "r", encoding="utf-8") as read_file, \
         open(__PROCESSED_CSV, "w", encoding="utf-8") as write_file:
        movie_data = __process_movie_data(read_file)
        movie_data = __discard__incomplete_records(movie_data)
        movie_data = [
            normalized for record in movie_data
            if (normalized := __normalize_movie_data(record))
        ]
        __write_processed_data(movie_data, write_file)


def __process_movie_data(read_file):
    processed_data = []
    reader = csv.DictReader(read_file)
    for row in reader:
        record = __load_omdb_data(row)
        record = __load_box_office_data(row, record)
        processed_data.append(record)
    return processed_data


def __load_omdb_data(row):
    movie_json = json.loads(row['omdb_data'])
    processed_record = {
        field: movie_json.get(field, "N/A") 
        for field in __movie_json_fieldnames
    }
    return processed_record


def __load_box_office_data(row, processed_record):
    box_office_json = json.loads(row['box_office_data'])
    for field in __box_office_json_fieldnames:
        amount_obj = box_office_json.get(field)
        if isinstance(amount_obj, dict):
            value = amount_obj.get("amount") or amount_obj.get("gross", {}).get("amount")
            processed_record[field] = value if value else "N/A"
        else:
            processed_record[field] = "N/A"
    return  processed_record


# uses the all() method to specify which records to keep
def __discard__incomplete_records(movie_data):
    return [
        record for record in movie_data
        if all(
            value != "N/A" and value != []
            for key, value in record.items()
            if key != "Awards"
        )
    ]


# fixes runtime, date, country, ratings, and director values
def __normalize_movie_data(record):
    record["Runtime"] = record["Runtime"].split(" ")[0]
    date_obj = datetime.strptime(record["Released"], "%d %b %Y")
    record["Released"] = date_obj.strftime("%Y/%m/%d")
    record["Country"] = record["Country"].split(",")[0].strip()
    record["Director"] = record["Director"].split(",")[0].strip()
    
    processed_ratings = []
    for row in record["Ratings"]:
        source = row.get("Source")
        raw_value = row.get("Value", "")
        clean_value = ""
        if source == "Internet Movie Database": 
            clean_value = raw_value.split("/")[0]
        elif source == "Rotten Tomatoes":
            num = raw_value.replace("%", "")
            clean_value = str(float(num) / 10)
        elif source == "Metacritic":
            num = raw_value.split("/")[0]
            clean_value = str(float(num) / 10)
        if clean_value: 
            processed_ratings.append(f"{source}:{clean_value}")
    
    if not processed_ratings: return None # invalid record
    record["Ratings"] = ", ".join(processed_ratings)
    return record


def __write_processed_data(movie_data, write_file):
    fieldnames = __movie_json_fieldnames + __box_office_json_fieldnames
    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(movie_data)
