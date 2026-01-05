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
__DATA_SIZE_LIMIT = 80000
__input_file = __DATA_DIR / "title.basics.tsv" 
__output_file = __BASE_DIR / "data" / "imdb_movie_ids.txt"
__movie_year = 2016  # change to filter movies by year


def extract_txt():
    row_count = 0
    with open(__input_file, "r", encoding="utf-8") as tsv_file, open(__output_file, "w", encoding="utf-8") as txt_file:
        reader = csv.DictReader(tsv_file, delimiter="\t")

        for row in reader:
            if row_count >= __DATA_SIZE_LIMIT: break
            start_year = row["startYear"]
            if start_year == r"\N":
                continue
            if row["titleType"] == "movie" and int(start_year) >= __movie_year:
                txt_file.write(row["tconst"] + "\n")
                row_count += 1

    print("Extraction complete.")
