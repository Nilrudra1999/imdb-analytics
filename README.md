# IMDb Analytics

An end-to-end data analytics system that pulls IMBd movie data from APIs through an ETL pipeline, to analyze historical trends over the past 10-20 years and create future movie predictions. The tech stack used for this project includes:

- python to script the ETL pipeline
- airflow to managing the script execution
- power BI for data visualization
- SSMS & local Microsoft Express SQL Server for data warehousing
- github for version control and presenting final reports
- OBS & Microsoft Clipchamp for video report creation

### System Structure

![System structure end-to-end](<system structure.png>)

### Data Sources Used

This project uses two third-party APIs as its data sources with varying uses. The IMDbAPI is used exclusively to pull detailed movie revenue information using a GET route with specific movie IDs. Meanwhile, the OMDb API acquires all other movie information such as release dates, ratings, casts members, awards, and etc. through API key dependant routes.<br>

<b>OMDb API</b>, [The Open Movie Database](https://www.omdbapi.com/) published over 10 years ago<br>
Made by Brian Fritz, and licensed under CC BY-NC 4.0<br>
Routes most used throughout this project:

- //?t=[some title spaces filled with '+']&apikey=########

<b>IMDbAPI</b> [Free IMDb API](https://imdbapi.dev/) published on January 2024<br>
Routes most used throughout this project:

- /search/titles
- /titles/{titleId}/boxOffice

### Relational Database Structure

![Relational database tables structure](<relational database tables structure.png>)

---

<b>Author:</b> Nilrudra Mukhopadhyay<br>
<b>Project start date:</b> 26-12-2025<br>
<b>Project end date:</b> N/A
