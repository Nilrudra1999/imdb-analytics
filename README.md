# IMDb Analytics

An exploratory data analysis project which examines movies trends from the past 10 years, using IMDb data that was collected from public APIs. The project uses an ETL pipeline for data acquisition, a local Microsoft SQL express server for data warehousing, and Power-BI reports for data visualizations. The [report](#report) section of this README displays the movie trends meanwhile, the [systems design](#systems-design) section showcases diagrams about the project's ETL pipeline and data infrastructure.

## Report

Final report (coming soon).

## Systems Design

Project's system consists of [Python scripts](/ETL%20scripts/) for extracting, cleaning, and loading the data, along with [T-SQL scripts](/SQL%20scripts/) for querying the data.

### ETL Pipeline Breakdown

![ETL breakdown diagram](/systems%20design/ETL%20breakdown.png)

The above diagram shows the execution paths for the ETL pipeline. When provided with an argument it either outputs IDs into a text file, or loads API data into the data warehouse. The pipeline is run within a local virtual environment with the following [specs](/systems%20design/requirements.txt).

### Data Warehouse/Database Schema

![Database schema](/systems%20design/database%20schema.png)

The above diagram shows the schema used to create this project's data warehouse. It follows typical relational database conventions with the added constraint that most tables won't accept NULL values since relationships between movies, ratings, revenues, and cast members is imperative for the analytics. The above schema was also used during the creation of the SQL [setup](/SQL%20scripts/database_setup.sql) and [testing](/SQL%20scripts/database_test.sql) scripts.

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
