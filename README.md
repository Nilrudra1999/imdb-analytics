# IMDb Analytics

This repository contains an end-to-end data analytics project examining IMDb historical movie data from 2015 till today. The [report](#report) extracts analytics from the data through various visualizations and outlines movie predictions based off the evidence. Additionally, the [systems design](#systems-design) section of this project showcases details about the project's ETL pipeline, and data warehousing.

## Report

Final report (coming soon).

## Systems Design

The system for this project is comprised of two parts. The [ETL pipeline](/ETL%20scripts/) for data acquisition, and the data warehouse for data integration. The pipeline consists of python scripts managed by a virtual environment, while the warehouse is built on a local Microsoft SQL express server managed using SSMS and [T-SQL scripts](/SQL%20scripts/)

### ETL Pipeline Breakdown

![ETL breakdown diagram](/systems%20design/ETL%20breakdown.png)

The main python script executes based on provided arguments, and either outputs IDs into a text file or loads API data into the data warehouse. All python scripts are written with a single public method and several private helper methods to maintain modularity, but doesn't follow conventional OOP rules.

The virtual environment specifications can be found within the [requirements text file](/systems%20design/requirements.txt) used while running this ETL pipeline.

### Data Warehouse/Database Schema

![Database schema](/systems%20design/database%20schema.png)

The schema follows the standards of a typical relational database, with the added constraint that most tables won't accept NULL values at all. Since this project's analytics rely on the relationship between movies, their ratings, revenues, and cast members, it was important to place NOT NULL constraints into the tables.

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
