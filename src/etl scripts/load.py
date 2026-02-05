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
import pandas as pd
import re
import pyodbc

__CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=ADMINISTRATOR\\SQLEXPRESS;"
    "Database=imdb_analytics_database;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

__MOVIE_DATA = {}


def store_processed_movie_data(base_directory):
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    df = pd.read_csv(processed_csv, keep_default_na=False)
    connection, cursor = __open_db_connection()
    records = df.to_dict('records')
    record_cnt = 0
    for record in records:
        __get_database_data(record)
        dir_id   = __insert_into_directors(cursor)
        movie_id = __insert_into_movies(dir_id, cursor)
        __insert_into_revenues(movie_id, cursor)
        __insert_into_awards(movie_id, cursor)
        __insert_into_ratings(movie_id, cursor)
        __insert_into_genres(movie_id, cursor)
        __insert_into_writers(movie_id, cursor)
        __insert_into_actors(movie_id, cursor)
        record_cnt += 1
    __close_db_connection(connection, cursor)
    print(f"Added {record_cnt} records to the database.")



def __get_database_data(record):
    global __MOVIE_DATA
    wins = nominations = None
    __MOVIE_DATA = {
        "director_name": record.get("Director"),
        "title": record.get("Title"),
        "runtime": record.get("Runtime"),
        "release": record.get("Released"),
        "country": record.get("Country"),
        "writers": [w.strip() for w in str(record.get("Writer", "")).split(",")],
        "actors":  [a.strip() for a in str(record.get("Actors", "")).split(",")],
        "genres":  [g.strip() for g in str(record.get("Genre", "")).split(",")],
        "ratings": [r.strip() for r in str(record.get("Ratings", "")).split(",")],
        "prod_bg": float(record.get("productionBudget")),
        "dome_gr": float(record.get("domesticGross")),
        "intr_gr": float(record.get("worldwideGross")),
        "op_w_gr": float(record.get("openingWeekendGross"))
    }
    raw_awards = str(record.get("Awards", ""))
    if raw_awards and raw_awards != "N/A":
        win_match = re.search(r'(\d+)\s+win', raw_awards, re.IGNORECASE)
        nom_match = re.search(r'(\d+)\s+nomination', raw_awards, re.IGNORECASE)
        if win_match: wins = win_match.group(1)
        if nom_match: nominations = nom_match.group(1)
    __MOVIE_DATA["awards"] = [wins, nominations]



def __insert_into_directors(cursor):
    id = 0
    name = __MOVIE_DATA["director_name"]
    cursor.execute("select director_id from directors where director_name = ?", (name,))
    result = cursor.fetchone()
    if result: id = result[0]
    else:
        id = __get_max_id("select max(director_id) from directors", cursor)
        cursor.execute("insert into directors values (?, ?)", (id, name,))
    return id


def __insert_into_genres(movie_id, cursor):
    id = __get_max_id("select max(genre_id) from genres", cursor)
    if __MOVIE_DATA["genres"] == "N/A": return
    for genre in __MOVIE_DATA["genres"]:
        cursor.execute("select genre_id from genres where genre_name = ?", (genre,))
        result = cursor.fetchone()
        if result:
            cursor.execute("insert into associated_genres values (?, ?)",
                           (movie_id, result[0]))
        else:
            cursor.execute("insert into genres values (?, ?)", (id, genre))
            cursor.execute("insert into associated_genres values (?, ?)", (movie_id, id))
            id = id + 1


def __insert_into_writers(movie_id, cursor):
    id = __get_max_id("select max(writer_id) from writers", cursor)
    if __MOVIE_DATA["writers"] == "N/A": return
    for writer in __MOVIE_DATA["writers"]:
        cursor.execute("select writer_id from writers where writer_name = ?", (writer,))
        result = cursor.fetchone()
        if result:
            cursor.execute("insert into associated_writers values (?, ?)",
                           (movie_id, result[0]))
        else:
            cursor.execute("insert into writers values (?, ?)", (id, writer))
            cursor.execute("insert into associated_writers values (?, ?)", (movie_id, id))
            id = id + 1


def __insert_into_actors(movie_id, cursor):
    id = __get_max_id("select max(actor_id) from actors", cursor)
    if __MOVIE_DATA["actors"] == "N/A": return
    for actor in __MOVIE_DATA["actors"]:
        cursor.execute("select actor_id from actors where actor_name = ?", (actor,))
        result = cursor.fetchone()
        if result:
            cursor.execute("insert into associated_actors values (?, ?)",
                           (movie_id, result[0]))
        else:
            cursor.execute("insert into actors values (?, ?)", (id, actor))
            cursor.execute("insert into associated_actors values (?, ?)", (movie_id, id))
            id = id + 1


def __insert_into_movies(dir_id, cursor):
    title   = __MOVIE_DATA["title"]
    runtime = __MOVIE_DATA["runtime"]
    release = __MOVIE_DATA["release"]
    country = __MOVIE_DATA["country"]
    id = __get_max_id("select max(movie_id) from movies", cursor)
    cursor.execute("insert into movies values (?, ?, ?, ?, ?, ?)",
                   (id, title, release, runtime, country, dir_id))
    return id


def __insert_into_revenues(movie_id, cursor):
    prod_budget = __MOVIE_DATA["prod_bg"]
    domestic_gr = __MOVIE_DATA["dome_gr"]
    interntl_gr = __MOVIE_DATA["intr_gr"]
    opening_wkd = __MOVIE_DATA["op_w_gr"]
    id = __get_max_id("select max(revenue_id) from revenues", cursor)
    cursor.execute(
        "insert into revenues values (?, ?, ?, ?, ?, ?)",
        (id, movie_id, prod_budget, domestic_gr, interntl_gr, opening_wkd)
    )


def __insert_into_ratings(movie_id, cursor):
    id = __get_max_id("select max(rating_id) from ratings", cursor)
    for rating in __MOVIE_DATA["ratings"]:
        ptrs = rating.split(":", 1)
        src  = ptrs[0].strip()
        val  = int(float(ptrs[1].strip()))
        cursor.execute("insert into ratings values (?, ?, ?, ?)", 
                       (id, movie_id, src, val))
        id = id + 1


def __insert_into_awards(movie_id, cursor):
    wins = __MOVIE_DATA["awards"][0]
    nominations = __MOVIE_DATA["awards"][1]
    cursor.execute(
        "insert into awards values (?, ?, ?)",
        (movie_id, wins, nominations)
    )


def __get_max_id(stmt: str, cursor):
    cursor.execute(stmt)
    id_result = cursor.fetchone()
    if id_result[0] is not None: curr_max = id_result[0]
    else: curr_max = 0
    return curr_max + 1


def __open_db_connection():
    connection = pyodbc.connect(__CONNECTION_STRING, autocommit=True)
    cursor = connection.cursor()
    return connection, cursor


def __close_db_connection(conn, cursor):
    cursor.close()
    conn.close()
