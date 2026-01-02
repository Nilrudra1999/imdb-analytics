from pathlib import Path
import csv

__BASE_DIR = Path(__file__).resolve().parent.parent
__DATA_DIR = __BASE_DIR / "data"
__input_file = __DATA_DIR / "title.basics.tsv" 
__output_file = __BASE_DIR / "data" / "imdb_movie_ids.txt"
__movie_ytd = 2016  # change to filter movies by year


# Reads the publicly available IMDb .tsv file, found in the data folder
# generates a .txt file with IMDb movie Ids with start years, beyond 2016
def extract_txt_with_ids():
    with open(__input_file, "r", encoding="utf-8") as tsv_file, open(__output_file, "w", encoding="utf-8") as txt_file:
        reader = csv.DictReader(tsv_file, delimiter="\t")

        for row in reader:
            start_year = row["startYear"]
            if start_year == r"\N":
                continue
            if row["titleType"] == "movie" and int(start_year) >= __movie_ytd:
                txt_file.write(row["tconst"] + "\n")

    print("Extraction complete.")
