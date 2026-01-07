"""----------------------------------------------------------------------------
    Main File - main entry point of the ETL pipeline
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This automation script controls the overall execution of the pipeline
    extracting IMDb movie IDs from the public dataset, fetching all
    related JSON info from the APIs, cleaning, and loading that data.
----------------------------------------------------------------------------"""
import argparse
from pathlib import Path
import movie_id_selector, extract, transform, load

BASE_DIRECTORY = Path(__file__).resolve().parent.parent

def process_imdb_ids():
    movie_id_selector.extract_ids_from_dataset(BASE_DIRECTORY)


def process_imdb_data():
    # extract.fetch_movie_data_from_api(BASE_DIRECTORY)
    # transform.parse_raw_movie_data(BASE_DIRECTORY)
    load.store_processed_movie_data(BASE_DIRECTORY)


def main():
    parser = argparse.ArgumentParser(description="IMDb ETL pipeline")
    parser.add_argument(
        "command",
        choices=["IDs", "data"],
        help="Either run 'IDs' or 'data' select arg"
    )
    args = parser.parse_args()
    if args.command   == "IDs":  process_imdb_ids()
    elif args.command == "data": process_imdb_data()


if __name__ == "__main__":
    main()
