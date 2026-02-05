"""----------------------------------------------------------------------------
    Main Transformer File - Transforms raw CSV data to tabular format
    -----------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    -----------------------------------------------------------------------
    This script uses the data/raw/data.csv and data/processed/data.csv
    files to transform the raw csv data into a more tabular format 
    after cherry picking the necessary information needed for the DB.
----------------------------------------------------------------------------"""
import pandas as pd
from json import loads

__MOVIE_JSON_FIELDNAMES = [
    "Title", "Runtime", "Released", "Country", 
    "Director", "Writer", "Actors",
    "Genre", "Ratings", "Awards"
]

__BOX_OFFICE_JSON_FIELDNAMES = [
    "productionBudget", "domesticGross",
    "worldwideGross", "openingWeekendGross"
]


def parse_raw_movie_data(base_directory):
    raw_csv = base_directory / "data" / "raw" / "data.csv"
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    df_raw = pd.read_csv(raw_csv)
    
    omdb_df = pd.json_normalize(df_raw['omdb_data'].apply(loads))
    box_office_df = df_raw['box_office_data'].apply(loads).apply(__extract_box_office)
    box_office_df = pd.DataFrame(box_office_df.tolist())
    df = pd.concat([omdb_df[__MOVIE_JSON_FIELDNAMES], box_office_df[__BOX_OFFICE_JSON_FIELDNAMES]], axis=1)
    required = ["Title", "Runtime", "Released", "Country", "Director", "productionBudget"]
    
    df.replace("N/A", pd.NA, inplace=True)
    df.dropna(subset=required, inplace=True)
    df = __normalize_dataframe(df)
    df.to_csv(processed_csv, index=False)



def __extract_box_office(entry):
    extracted = {}
    for field in __BOX_OFFICE_JSON_FIELDNAMES:
        object = entry.get(field)
        if isinstance(object, dict):
            val = object.get("amount") or object.get("gross", {}).get("amount")
            extracted[field] = val
        else: extracted[field] = None
    return extracted


# fixes runtime, date, country, ratings, and director values in movie records
def __normalize_dataframe(df):
    df['Runtime']  = df['Runtime'].str.split(" ").str[0]
    df['Released'] = pd.to_datetime(df['Released'], format='%d %b %Y').dt.strftime('%Y/%m/%d')
    df['Country']  = df['Country'].str.split(",").str[0].str.strip()
    df['Director'] = df['Director'].str.split(",").str[0].str.strip()
    df['Ratings']  = df['Ratings'].apply(__process_ratings_list)
    df['productionBudget'] = pd.to_numeric(df['productionBudget'], errors='coerce')
    df['domesticGross']    = pd.to_numeric(df['domesticGross'], errors='coerce').fillna(df['productionBudget'] * 1.5).astype(int)
    df['worldwideGross']   = pd.to_numeric(df['worldwideGross'], errors='coerce').fillna(df['productionBudget'] * 1.5).astype(int)
    df['openingWeekendGross'] = pd.to_numeric(df['openingWeekendGross'], errors='coerce').fillna(df['productionBudget'] * 0.2).astype(int)
    return df


def __process_ratings_list(ratings):
    if not isinstance(ratings, list) or len(ratings) == 0: return "House Rating:8.5"
    processed = []
    for rating in ratings:
        src, val = rating.get("Source"), rating.get("Value", "")
        clean = None
        if   src == "Internet Movie Database": clean = float(val.split("/")[0])
        elif src == "Rotten Tomatoes": clean = float(val.replace("%", "")) / 10
        elif src == "Metacritic": clean = float(val.split("/")[0]) / 10
        if clean is not None:
            if clean < 1.0: clean *= 10.0
            processed.append(f"{src}:{clean}")
    return ", ".join(processed) if processed else "House Rating:8.5"
