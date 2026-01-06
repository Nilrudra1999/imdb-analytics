"""----------------------------------------------------------------------------
    ID Extractor File - uses an IMDb dataset & a year to extract IDs
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This script extracts IDs from the publicly available IMDb dataset,
    using the title type of "movie", and a benchmark year to filter the 
    records. Then writes the IDs into a .txt file.
----------------------------------------------------------------------------"""
import csv
from pathlib import Path

__BASE_DIR = Path(__file__).resolve().parent.parent
__DATA_DIR = __BASE_DIR / "data"
__tsv_file = __DATA_DIR / "title.basics.tsv" 
__text_file = __BASE_DIR / "data" / "imdb_movie_ids.txt"
__start_year = 2015  # change to filter movies by year


def load_text_file_with_imdbIDs():
    with open(__tsv_file, "r", encoding="utf-8") as read_file, \
         open(__text_file, "w", encoding="utf-8") as write_file:
        csv_reader = csv.DictReader(read_file, delimiter="\t")

        for row in csv_reader:
            if row["startYear"] == r"\N": continue
            if row["titleType"] == "movie" and int(row["startYear"]) >= __start_year:
                write_file.write(row["tconst"] + "\n")

    print("Extraction complete.")
