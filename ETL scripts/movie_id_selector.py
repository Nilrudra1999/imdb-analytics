"""----------------------------------------------------------------------------
    ID Selector File - uses an IMDb dataset & a filter year to get IDs
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This script extracts IDs from the publicly available IMDb dataset,
    using the title type of "movie", and a benchmark year to filter the 
    records. Then writes the IDs into a .txt file.
----------------------------------------------------------------------------"""
from csv import DictReader

__start_year = 2015  # filter movies by year

def extract_ids_from_dataset(base_directory):
    data_directory = base_directory / "data"
    tsv_file  = data_directory / "title.basics.tsv"
    text_file = base_directory / "data" / "imdb_movie_ids.txt"
    
    reader_file = __open_reader_file(tsv_file)
    writer_file = __open_writer_file(text_file)
    
    tsv_records = DictReader(reader_file, delimiter="\t")
    for record in tsv_records:
        if record["startYear"] == r"\N": continue
        if record["titleType"] == "movie" and int(record["startYear"]) >= __start_year:
            writer_file.write(record["tconst"] + "\n")
    print("Movie Id extraction complete.")


def __open_reader_file(dataset):
    reader_file = open(dataset, "r", encoding="utf-8")
    return reader_file


def __open_writer_file(dataset):
    writer_file = open(dataset, "w", encoding="utf-8")
    return writer_file
