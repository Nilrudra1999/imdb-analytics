# File Success Predictor

<b>Author:</b> Nilrudra Mukhopadhyay<br>
<b>Project Type:</b> Predictive Analytics and Data warehousing project - independently built<br>

## Project Overview

The purpose of the project is to develope a set of machine learning models which can predict, as accurately as possible, how much revenue a potential movie would generate given information such as the Director, Genre, Production Budget, Lead Actor, and Writer. A User Interface wrapper is provided to allow non-technical people to utilize the models with ease.

### Business Purpose:

A studio looking to make new movies always risks investing into a project that won't be profitable. This can happen from green-lighting a project out of emotions, biases, or general human error as such, a neutral tool such as this app can augment a studio's decision making process, resulting in better turnovers.

### Tech Stack:

- Python
- Jupyter-NoteBooks
- Scikit-learn
- CustomTkinter
- MatPlotLib
- Pandas & Numpy
- Microsoft SQL express server
- Microsoft SQL sever management studio (SSMS)
- Visual studio code
- Git bash/Github

## Data Organization

The data is stored in a database. (schema, ETL pipeline, and use specifics later)

### Data Sources:

- [OMDb API open IMDb database, IMDb ID based](https://www.omdbapi.com/)
- [Free IMDb API, IMDb ID based](https://imdbapi.dev/)
- [Publicly available IMDb dataset, ID fragment](/data/imdb_movie_ids.txt)

## Machine Learning Models

How is success defined?

- opening weekend rev
- domestic gross rev
- international gross rev
- metacritic, rotten tomatoes, and internet database ratings

What will be used to measure potential success then?

- director: a good director (good success record) indicates good rev
- genre: a popular genre (changes historically) can mean that the movie might have more viewer
- production budget: for certain genres lower budgets produce better results and vis-versa
- actor & writer: including some make the movies more successful while others not

### Unsupervised Learning Trends

### Supervised Learning Models Used
