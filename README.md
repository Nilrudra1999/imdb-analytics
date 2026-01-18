# IMDb Analytics

This end-to-end data analytics project examines historical IMDb movie data from 2015 till today. The [report](#report) extracts analytics from the data through visualizations and outlines movie predictions based off the evidence. Additionally, the [systems design](#systems-design) showcases details about the project's ETL pipeline, and data warehousing infrastructure.

## Report

Final report (coming soon).

## Systems Design

This project is comprised of two parts, the [ETL pipeline](/ETL%20scripts/) for data acquisition, and the data warehouse for data integration. The pipeline consists of python scripts managed by a virtual environment, while the warehouse is built on a local Microsoft SQL express server managed using SSMS and [T-SQL scripts](/SQL%20scripts/)

### ETL Pipeline Breakdown

![ETL breakdown diagram](/systems%20design/ETL%20breakdown.png)

The main python script executes based on provided arguments, and either outputs IDs into a text file or loads API data into a database. All python scripts are written with a single public method and several private helper methods to maintain modularity, but doesn't follow conventional OOP practice.

The virtual environment specifications can be found within the [requirements text file](/systems%20design/requirements.txt) used while running this ETL pipeline.

### Data Warehouse/Database Schema

![Database schema](/systems%20design/database%20schema.png)

The schema follows the standards of a typical relational database, with the added constraint that most tables won't accept NULL values. Since this project relies on the relationship between movies, their ratings, revenues, and cast members, it was imperative to place NOT NULL constraints on these tables.

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
