"""----------------------------------------------------------------------------
    Main File - main entry point of the ETL pipeline
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This automation script controls the overall execution of the pipeline
    from extracting IMDb movie IDs from the public dataset, extracting
    all related JSON info from the APIs, cleaning, and loading that data.
----------------------------------------------------------------------------"""
import argparse
import imdb_id_extractor, extract, transform

def get_movieIDs_from_tsv():
    imdb_id_extractor.load_text_file_with_imdbIDs()


def get_movie_data():
    extract.process_movie_data_extraction()
    transform.process_movie_data_transformations()
    # load.transfer_movies_into_database()


def main():
    parser = argparse.ArgumentParser(description="IMDb ETL pipeline")
    parser.add_argument(
        "command",
        choices=["get_ids", "get_data"],
        help="Which process to run"
    )
    args = parser.parse_args()
    # filter movie IDs from the public tsv file
    if args.command == "get_ids": get_movieIDs_from_tsv()
    # run the actual ETL pipeline based on collected IDs
    elif args.command == "get_data": get_movie_data()


if __name__ == "__main__":
    main()
