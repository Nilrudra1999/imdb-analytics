# IMDb Analytics

This repository contains an end-to-end data analytics project examining IMDb historical movie data from 2015 till today. The [report](#report) analyzes the data through various visualizations and breaks down its meaning, then outlines numerous movie predictions based off the gathered evidence. Additionally, the [systems design](#systems-design) section of this project showcases details about the project's ETL pipeline, data filters, and data warehousing.

## Report

Final report (coming soon).

## Systems Design

The system used for this project is comprised of two parts. First is the [ETL pipeline](/ETL%20scripts/) for data acquisition, using python scripts and a python virtual environment to operate. Second is the data warehouse for data integration, using a local Microsoft SQL express server that is managed through SQL Server Management Studio (SSMS) and [T-SQL scripts](/SQL%20scripts/).

### ETL Pipeline Breakdown

![ETL breakdown diagram](/systems%20design/ETL%20breakdown.png)

The main python script follows a path of execution based on provided arguments, and either outputs IMDb IDs into a text file or loads API data into a local database using the ETL pipeline. All scripts are written with a single public method and several private helper methods to maintain modularity, but doesn't follow conventional OOP rules.

The virtual environment specifications can be found within the [requirements text file](/systems%20design/requirements.txt) used while running this ETL pipeline.

### Data filters

The following pieces of information were checked to ensure no NULL values were present:

- <b>movies table:</b> title, runtime, release date, country of origin, and at one director's name
- <b>writers table:</b> names of one or more writers
- <b>actors table:</b> names of one or more actors
- <b>genres table:</b> names of one or more genres
- <b>ratings table:</b> if it belonged to either Internet movie db, Rotten tomatoes, or Metacritic
- <b>revenues table:</b> the budget, domestic and international gross profit, and the opening weekend profit
- <b>awards table:</b> this one could have either wins, nominations, both or none (only exception for NULL values)

### Database Schema

![Database schema](/systems%20design/database%20schema.png)

The schema follows the standards of a typical relational database with the added restriction that many tables won't accept incomplete data (NULL values) at all. Since this project's analytics rely on the relationship of movies and their ratings, revenues, and cast, it was important to place these constraints into the database from the start.

The above schema was also used during the creation of the SQL [setup](/SQL%20scripts/database_setup.sql) and [testing](/SQL%20scripts/database_test.sql) scripts.

### Data Sources:

- [OMDb API open IMDb database, IMDb ID based](https://www.omdbapi.com/)
- [Free IMDb API, IMDb ID based](https://imdbapi.dev/)
- [Publicly available IMDb dataset, ID fragment](/data/imdb_movie_ids.txt)

### Tech Stack:

- Python
- Microsoft SQL express server
- Microsoft SQL sever management studio (SSMS)
- Visual studio code
- PowerBI
- MS Excel
- Git bash/Github

---

<b>Author:</b> Nilrudra Mukhopadhyay<br>
<b>Project Type:</b> Data analyst portfolio project - independently built<br>
