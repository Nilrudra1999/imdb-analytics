/*****************************************************************************
			IMDb Analytics project - script for creating sql tables
------------------------------------------------------------------------------
Author: Nilrudra Mukhopadhyay
Email: nilrudram@gmail.com
------------------------------------------------------------------------------
The script executes the following in the same order as written below:
1. delete any prior tables if any are within the database
2. create tables with, primary/foreign keys, and not null constraints
*****************************************************************************/
use imdb_analytics_database;
go

drop table if exists dbo.ratings;
drop table if exists dbo.awards;
drop table if exists dbo.revenues;
drop table if exists dbo.associated_genres;
drop table if exists dbo.associated_actors;
drop table if exists dbo.associated_writers;
drop table if exists dbo.movies;
drop table if exists dbo.genres;
drop table if exists dbo.actors;
drop table if exists dbo.writers;
drop table if exists dbo.directors;


create table dbo.directors (
	director_id	  int primary key,
	director_name varchar(50) not null
);

create table dbo.writers (
	writer_id	int primary key,
	writer_name varchar(50) not null
);

create table dbo.actors (
	actor_id	int primary key,
	actor_name  varchar(50) not null
);

create table dbo.genres (
	genre_id	int primary key,
	genre_name  varchar(50) not null
);

create table dbo.movies (
	movie_id		int primary key,
	title			varchar(50) not null,
	release_date	date not null,
	runtime			int not null,
	country_of_origin	varchar(50) not null,
	director			int not null references dbo.directors(director_id)
);

create table dbo.associated_writers (
	movie_id  int not null references dbo.movies(movie_id),
	writer_id int not null references dbo.writers(writer_id)
);

create table dbo.associated_actors (
	movie_id int not null references dbo.movies(movie_id),
	actor_id int not null references dbo.actors(actor_id)
);

create table dbo.associated_genres (
	movie_id int not null references dbo.movies(movie_id),
	genre_id int not null references dbo.genres(genre_id)
);

create table dbo.revenues (
	revenue_id		int primary key,
	movie_id		int not null references dbo.movies(movie_id),
	prod_budget			decimal(15,2) not null,
	domestic_gross		decimal(15,2) not null,
	international_gross decimal(15,2) not null,
	opening_weekend		decimal(15,2) not null
);

create table dbo.awards (
	movie_id	int not null references dbo.movies(movie_id),
	award		varchar(50),
	nomination	varchar(50)
);

create table dbo.ratings (
	rating_id	 int primary key,
	movie_id	 int not null references dbo.movies(movie_id),
	rating_src	 varchar(50) not null,
	rating_value int not null,
);
