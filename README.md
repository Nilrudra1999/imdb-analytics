# IMDb Analytics

Found below is the [report](#report), with visualizations of the IMDb historical data, breaking down its meaning, and stating future movie predictions based off the evidence. Additionally, there is the [systems design](#systems-design) section, showcasing details about the ETL pipeline, data filtering, and data warehousing.

## Report

Final report (coming soon).

## Systems Design

The system used for this project is comprised of two parts. One is the [ETL pipeline](/ETL%20scripts/) for data acquisition, made of python scripts and run inside a python virtual environment. Another is the data warehouse for data integration, a local Microsoft SQL express server, managed through SQL Server Management Studio (SSMS) and [T-SQL scripts](/SQL%20scripts/).

### ETL Pipeline Breakdown

![ETL breakdown diagram](/systems%20design/ETL%20breakdown.png)

The main python script follows a set path of execution based on some arguments, and either outputs IMDb IDs into a txt file or loads API data into a local database using the ETL pipeline. All scripts are written with a single public method and several private helper methods to maintain modularity, but doesn't follow conventional OOP rules.

The virtual environment specifications can be found within the [requirements text file](/systems%20design/requirements.txt) used while running this ETL pipeline.

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
