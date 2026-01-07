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
from csv import DictReader, DictWriter
from json import loads
from datetime import datetime

__MOVIE_JSON_FIELDNAMES = [
    "Title", "Runtime", "Released", "Country", 
    "Director", "Writer", "Actors",
    "Genre", "Ratings", "Awards"
]

__BOX_OFFICE_JSON_FIELDNAMES = [
    "productionBudget", "domesticGross",
    "worldwideGross", "openingWeekendGross"
]


def parse_raw_movie_data(base_directory):
    raw_csv = base_directory / "data" / "raw" / "data.csv"
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    normalized_movie_data = []
    
    reader_file = __open_reader_file(raw_csv)
    writer_file = __open_writer_file(processed_csv)
    
    movie_data  = __parsing_data(reader_file)
    movie_data  = __discard__incomplete_records(movie_data)
    for record in movie_data:
        normalized = __normalize_movie_data(record)
        if normalized is not None: normalized_movie_data.append(normalized)
    movie_data = normalized_movie_data
    __write_processed_data(movie_data, writer_file)


def __open_reader_file(dataset):
    reader_file = open(dataset, "r", encoding="utf-8")
    return reader_file


def __open_writer_file(dataset):
    writer_file = open(dataset, "w", encoding="utf-8")
    return writer_file


def __parsing_data(dataset):
    processed_data = []
    records = DictReader(dataset)
    for record in records:
        movie_data = __load_omdb_data(record)
        movie_data = __load_box_office_data(record, movie_data)
        processed_data.append(movie_data)
    return processed_data


def __load_omdb_data(record):
    movie_json = loads(record['omdb_data'])
    processed_json = {}
    for field in __MOVIE_JSON_FIELDNAMES:
        value = movie_json.get(field, "N/A")
        processed_json[field] = value
    return processed_json


# box office data is kept as json of dict objects within raw API data
def __load_box_office_data(record, movie_data):
    box_office_json = loads(record['box_office_data'])
    for field in __BOX_OFFICE_JSON_FIELDNAMES:
        amount_obj = box_office_json.get(field)
        if isinstance(amount_obj, dict):
            value = amount_obj.get("amount") or amount_obj.get("gross", {}).get("amount")
            movie_data[field] = value if value else "N/A"
        else:
            movie_data[field] = "N/A"
    return  movie_data


def __discard__incomplete_records(movie_data):
    filtered_data = []
    for record in movie_data:
        is_valid = True
        for key, value in record.items():
            if key == "Awards": continue
            if value == "N/A" or value == []:
                is_valid = False
        if is_valid: filtered_data.append(record)
    return filtered_data


# fixes runtime, date, country, ratings, and director values in movie records
def __normalize_movie_data(movie_record):
    movie_record["Runtime"]  = movie_record["Runtime"].split(" ")[0]
    date_obj = datetime.strptime(movie_record["Released"], "%d %b %Y")
    movie_record["Released"] = date_obj.strftime("%Y/%m/%d")
    movie_record["Country"]  = movie_record["Country"].split(",")[0].strip()
    movie_record["Director"] = movie_record["Director"].split(",")[0].strip()
    
    processed_ratings = []
    for rating in movie_record["Ratings"]:
        source  = rating.get("Source")
        raw_value = rating.get("Value", "")
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
    movie_record["Ratings"] = ", ".join(processed_ratings)
    return movie_record


def __write_processed_data(movie_data, write_file):
    fieldnames = __MOVIE_JSON_FIELDNAMES + __BOX_OFFICE_JSON_FIELDNAMES
    csv_writer = DictWriter(write_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(movie_data)
