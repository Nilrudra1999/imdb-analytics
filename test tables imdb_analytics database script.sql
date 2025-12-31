/*****************************************************************************
		IMDb Analytics project - script for testing sql tables structure
------------------------------------------------------------------------------
Author: Nilrudra Mukhopadhyay
Email: nilrudram@gmail.com
------------------------------------------------------------------------------
The script performs the following actions on newly created tables:
1. insert & update single records into tables
2. insert & update multi-records into tables	
3. check not null constraints
4. check primary and foreign key constraints
5. delete all newly added records from tables
******************************************************************************/
use imdb_analytics;
go

-- single record insert statements (should execute successfully)
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


-- single record update statements (should execute without errors)
update dbo.movies set runtime = 4500, country_of_origin = 'Canada', title = 'First movie';
update dbo.genres set grn_name = 'Sci-fi' where genre_id = 101;
update dbo.writers set wtr_name = 'Robert J.' where writer_id = 101;
update dbo.actors set atr_name = 'Samuel Kim' where actor_id = 101;
update dbo.directors set dir_name = 'John Carpenter' where director_id = 101;
update dbo.awards set award = 'best screenplay', nomination = NULL where nomination = 'oscar';
update dbo.ratings set rtg_source = 'Blockbuster.com' where rtg_source = 'google';
update dbo.revenues set prod_budget = 75000150.55 where domestic_gross = 32000000.75;

-- following updates should fail, updating primary key when foreign keys reference it
update dbo.movies set movie_id = 102;
update dbo.actors set actor_id = 102;
update dbo.directors set director_id = 102;
update dbo.writers set writer_id = 102;
update dbo.genres set genre_id = 102;


-- multi-insert statements (should execute without errors)
insert into dbo.directors (director_id, dir_name)
values
	(102, 'Test Dir 2'),
	(103, 'Test Dir 3'),
	(104, 'Test Dir 4'),
	(105, 'Test Dir 5');

insert into dbo.writers (writer_id, wtr_name)
values
	(102, 'Test Writer 2'),
	(103, 'Test Writer 3'),
	(104, 'Test Writer 4'),
	(105, 'Test Writer 5');

insert into dbo.actors (actor_id, atr_name)
values
	(102, 'Test Actor 2'),
	(103, 'Test Actor 3'),
	(104, 'Test Actor 4'),
	(105, 'Test Actor 5');

insert into dbo.genres (genre_id, grn_name)
values
	(102, 'Adventure'),
	(103, 'Superhero'),
	(104, 'Medieval'),
	(105, 'Wester');

-- TODO - insert movies, associated tables, ratings, awards, and revenues
-- TODO - 2 rows each table update some records


-- insertion/updates check using select, join, and sub-select queries
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


-- TODO - check not null constraints by trying to insert/update with NULLs
-- TODO - delete the records added because of testing, db clean-up
