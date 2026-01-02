"""----------------------------------------------------------------------------
    Main File - main entry point of the ETL pipeline
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This automation script controls the overall execution of the pipeline
    from extracting IMDb movie IDs from the public dataset, extracting
    all related JSON info from the APIs, cleaning, and loading the data.
----------------------------------------------------------------------------"""
import imdb_id_extractor

def run_etl_processes():
    imdb_id_extractor.extract_txt_with_ids()
    
if __name__ == "__main__":
    run_etl_processes()
