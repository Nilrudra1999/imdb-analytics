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


def store_processed_movie_data(base_directory):
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    pass

