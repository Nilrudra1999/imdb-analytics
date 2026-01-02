import imdb_id_extractor

def run_etl_processes():
    imdb_id_extractor.extract_txt_with_ids()
    
if __name__ == "__main__":
    run_etl_processes()
