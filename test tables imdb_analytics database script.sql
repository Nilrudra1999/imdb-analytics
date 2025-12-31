/*****************************************************************************
		IMDb Analytics project - script for testing sql tables structure
------------------------------------------------------------------------------
Author: Nilrudra Mukhopadhyay
Email: nilrudram@gmail.com
------------------------------------------------------------------------------
The script executes the following in the same order as written below:

- insert & update single records into tables	(should be successful)
- insert & update multi-records into tables		(should be successful)
- check not null constraints					(should fail)
- check primary and foreign key constraints		(should fail)
- delete all newly added records from tables
******************************************************************************/
use imdb_analytics;
go

-- following statements should execute without errors if tables were constructed correctly
insert into dbo.directors values (101, 'test director 1');
insert into dbo.writers values (101, 'test writer 1');
insert into dbo.actors values (101, 'test actor 1');
insert into dbo.genres values (101, 'test genre 1');

insert into dbo.movies values (101, 'movie 1', 3600, '2010/05/11', 'USA', 101);
insert into dbo.associated_writers values (101, 101);
insert into dbo.associated_actors values (101, 101);
insert into dbo.associated_genres values (101, 101);

insert into dbo.revenues values (101, 101, 15500000.50, 32000000.75, 576002.15, 75649.00);
insert into dbo.awards values (101, 'best actor', NULL);
insert into dbo.awards values (101, NULL, 'oscar');
insert into dbo.ratings values (101, 'rotten tomato', 8, 101);
insert into dbo.ratings values (102, 'google', 6, 101);
insert into dbo.ratings values (103, 'amazon reviews', 7, 101);


-- insertion check using select, join, and sub-select queries
select * from dbo.movies;
select * from dbo.associated_writers;
select * from dbo.associated_actors;
select * from dbo.associated_genres;
select * from dbo.revenues;
select * from dbo.ratings;
select * from dbo.awards;
select * from dbo.genres;
select * from dbo.actors;
select * from dbo.writers;
select * from dbo.directors;


select movie_id, title, runtime, release_date, country_of_origin, 
	  (select dir_name from dbo.directors where director_id = director) 
	   as director_name
from dbo.movies;


select title, runtime, release_date, country_of_origin, 
	  (select wtr_name from dbo.writers w where w.writer_id = aw.writer_id)
	   as writer_name
from dbo.movies m 
join dbo.associated_writers aw
	on m.movie_id = aw.movie_id;


select title as 'movie name', country_of_origin, 
	  (select dir_name from dbo.directors where director_id = director)
	   as director,
	   rating_id, rtg_source as 'source', rtg_value as 'values 1-10',
	   prod_budget, domestic_gross as 'domestic', international_gross as 'internation'
from dbo.ratings rt 
join dbo.revenues re
	on rt.movie_id = re.movie_id
join dbo.movies mo
	on rt.movie_id = mo.movie_id;
