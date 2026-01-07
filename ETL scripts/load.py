"""----------------------------------------------------------------------------
    Main Loader File - Loads processed CSV data into local database
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This script uses data/processed/data.csv file to load the tabular, 
    normalized data from the APIs into the local database. This is the
    final step of the ETL pipeline for gathering imdb movie data. 
----------------------------------------------------------------------------"""
from csv import DictReader
import re
import pyodbc

__CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=ADMINISTRATOR\\SQLEXPRESS;"
    "Database=master;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

__director_name = ""
__title = "" 
__runtime = "" 
__release = "" 
__country = ""
__writers = []
__actors  = []
__genres  = []
__ratings = []
__awards  = []
__prod = 0
__domestic = 0
__international = 0 
__opening_weekend = 0


def store_processed_movie_data(base_directory):
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    connection, cursor = __open_db_connection()
    records = __get_records_from_csv(processed_csv)
    for record in records:
        __get_database_data(record)
        __set_database_data(connection, cursor)
    __close_db_connection(connection, cursor)


def __get_database_data(record):
    global __director_name, __writers, __actors, __genres
    global __title, __runtime, __release, __country
    global __prod, __domestic, __international, __opening_weekend
    global __ratings, __awards
    wins = ""
    nominations = ""
    
    __director_name = record.get("Director")
    __title   = record.get("Title")
    __runtime = record.get("Runtime")
    __release = record.get("Released")
    __country = record.get("Country")
    
    __writers = [w.strip() for w in record.get("Writer", "").split(",")]
    __actors  = [a.strip() for a in record.get("Actors", "").split(",")]
    __genres  = [g.strip() for g in record.get("Genre", "").split(",")]
    __ratings = [r.strip() for r in record.get("Ratings", "").split(",")]
    
    __prod = int(record.get("productionBudget", 0))
    __domestic = int(record.get("domesticGross", 0))
    __international = int(record.get("worldwideGross", 0))
    __opening_weekend = int(record.get("openingWeekendGross", 0))
    
    raw_awards = record.get("Awards", "")
    if raw_awards and raw_awards != "N/A":
        win_match = re.search(r'(\d+)\s+win', raw_awards, re.IGNORECASE)
        nom_match = re.search(r'(\d+)\s+nomination', raw_awards, re.IGNORECASE)
        wins = win_match.group(0) if win_match else ""
        nominations = nom_match.group(0) if nom_match else ""
    __awards = [wins, nominations]



def __set_database_data(connection, cursor):
    pass


def __get_records_from_csv(reader_file):
    reader = open(reader_file, "r", encoding="utf-8")
    return DictReader(reader)


def __open_db_connection():
    try:
        connection = pyodbc.connect(__CONNECTION_STRING)
        cursor = connection.cursor()
        print("DB connection successful")
        return connection, cursor
    except pyodbc.Error as err:
        print(f"DB connection failed: {err}")
        return None, None


def __close_db_connection(conn, cursor):
    cursor.close()
    conn.close()
    print("DB connection closed successfully")
