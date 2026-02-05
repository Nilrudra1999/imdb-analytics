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
*****************************************************************************/
use imdb_analytics_database;
go

-- following insert stmts should execute without errors
insert into dbo.directors values (101, 'test director 1');
insert into dbo.writers   values (101, 'test writer 1');
insert into dbo.actors    values (101, 'test actor 1');
insert into dbo.genres    values (101, 'test genre 1');

insert into dbo.movies	values (101, 'movie 1', 3600, '2010/05/11', 'USA', 101);
insert into dbo.associated_writers values (101, 101);
insert into dbo.associated_actors  values (101, 101);
insert into dbo.associated_genres  values (101, 101);

insert into dbo.revenues values (101, 101, 15500000.50, 32000000.75, 576002.15, 75649.00);
insert into dbo.awards   values (101, 'best actor', NULL);
insert into dbo.awards   values (101, NULL, 'oscar');
insert into dbo.ratings  values (101, 'rotten tomato', 8, 101);
insert into dbo.ratings  values (102, 'google', 6, 101);
insert into dbo.ratings  values (103, 'amazon reviews', 7, 101);


-- following update stmts should execute without errors
update dbo.movies  set runtime = 4500, country_of_origin = 'Canada', title = 'First movie';
update dbo.genres  set genre_name = 'Sci-fi'	 where genre_id = 101;
update dbo.writers set writer_name = 'Robert J.' where writer_id = 101;
update dbo.actors  set actor_name = 'Samuel Kim' where actor_id = 101;

update dbo.directors set director_name = 'John Carpenter' where director_id = 101;
update dbo.awards	 set award = 'best screenplay', nomination = NULL where nomination = 'oscar';
update dbo.ratings	 set rating_src = 'Blockbuster.com' where rating_src = 'google';
update dbo.revenues  set prod_budget = 75000150.55		where domestic_gross = 32000000.75;
-- following updates should fail (updating PK when FKs reference it) 
update dbo.movies	 set movie_id = 102;
update dbo.actors	 set actor_id = 102;
update dbo.directors set director_id = 102;
update dbo.writers	 set writer_id = 102;
update dbo.genres	 set genre_id = 102;


-- multi-insert stmts should execute without errors
insert into dbo.directors (director_id, director_name)
values
	(102, 'Test Dir 2'),
	(103, 'Test Dir 3'),
	(104, 'Test Dir 4'),
	(105, 'Test Dir 5');

insert into dbo.writers (writer_id, writer_name)
values
	(102, 'Test Writer 2'),
	(103, 'Test Writer 3'),
	(104, 'Test Writer 4'),
	(105, 'Test Writer 5');

insert into dbo.actors (actor_id, actor_name)
values
	(102, 'Test Actor 2'),
	(103, 'Test Actor 3'),
	(104, 'Test Actor 4'),
	(105, 'Test Actor 5');

insert into dbo.genres (genre_id, genre_name)
values
	(102, 'Adventure'),
	(103, 'Superhero'),
	(104, 'Medieval'),
	(105, 'Wester');

insert into dbo.movies (movie_id, title, release_date, runtime, country_of_origin, director)
values
	(102, 'New movie 2', '2021/06/22', 7599, 'Finland', 103),
	(103, 'New movie 3', '2022/06/22', 1199, 'Finland', 104),
	(104, 'New movie 4', '2018/04/14', 4509, 'USA', 102),
	(105, 'New movie 5', '2021/01/05', 5007, 'Canada', 103),
	(106, 'New movie 6', '2018/04/11', 2309, 'USA', 105);

insert into dbo.associated_genres (movie_id, genre_id)
values
	(102, 104),
	(103, 104),
	(104, 103),
	(105, 105),
	(106, 102);

insert into dbo.associated_writers (movie_id, writer_id)
values
	(102, 104),
	(103, 102),
	(104, 105),
	(105, 105),
	(106, 103);

insert into dbo.associated_actors (movie_id, actor_id)
values
	(102, 105),
	(103, 104),
	(104, 102),
	(105, 102),
	(106, 103);

insert into dbo.ratings (rating_id, movie_id, rating_src, rating_value)
values
	(104, 102, 'google reviews', 5),
	(105, 102, 'amazon reviews', 6),
	(106, 102, 'rotten tomato', 5),
	(107, 103, 'google reviews', 7),
	(108, 103, 'Blockbuster.com', 8),
	(109, 104, 'rotten tomato', 9),
	(110, 104, 'google reviews', 8),
	(111, 105, 'rotten tomato', 3),
	(112, 105, 'amazon reviews', 4),
	(113, 105, 'Blockbuster.com', 3),
	(114, 106, 'google reviews', 5),
	(115, 106, 'rotten tomato', 6);

insert into dbo.awards (movie_id, award, nomination)
values
	(102, NULL, NULL),
	(103, 'best writter', NULL),
	(103, 'best screenplay', NULL),
	(103, NULL, 'best motion picture'),
	(104, NULL, 'oscar'),
	(104, 'best motion picture', NULL),
	(104, 'best actor', NULL),
	(105, NULL, NULL),
	(106, NULL, 'best sound acting');

insert into dbo.revenues (revenue_id, movie_id, prod_budget, domestic_gross, international_gross, opening_weekend)
values
	(102, 102, 35500000.00, 17566100.50, 13350000.55, 11500.17),
	(103, 103, 700500117.35, 17566100.50, 13350000.55, 11500.17),
	(104, 104, 13000000.55, 13000500.00, 70500600.55, 145000.41),
	(105, 105, 750500000.11, 17566100.50, 13350000.55, 11500.17),
	(106, 106, 14500000.55, 17566100.50, 13350000.55, 345000.55);


-- multi-update stmts should execute without errors
update dbo.ratings   set rating_value = 10 where rating_src = 'google reviews';
update dbo.revenues  set international_gross = 15500050.17 where movie_id > 103;
update dbo.awards	 set nomination = 'best record tester' where nomination is NULL;
update dbo.directors set director_name = 'John db-rec tester doe' where director_id > 101;


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
	(select director_name from dbo.directors where director_id = director) as director_name
from dbo.movies;

select title, runtime, release_date, country_of_origin, 
	(select writer_name from dbo.writers w where w.writer_id = aw.writer_id) as writer_name
from dbo.movies m 
join dbo.associated_writers aw
  on m.movie_id = aw.movie_id;

select title as 'movie name', country_of_origin, 
	(select director_name from dbo.directors where director_id = director) as 'director',
	 rating_id, rating_src as 'source', rating_value as 'values 1-10',
	 prod_budget, domestic_gross as 'domestic', international_gross as 'internation'
from dbo.ratings rt 
join dbo.revenues re
  on rt.movie_id = re.movie_id
join dbo.movies mo
  on rt.movie_id = mo.movie_id;

select m.movie_id, m.title, 
	(select actor_name from dbo.actors a       where a.actor_id = aa.actor_id)   as 'actor',
	(select writer_name from dbo.writers w     where w.writer_id = aw.writer_id) as 'writer', 
	(select director_name from dbo.directors d where d.director_id = m.director) as 'director name',
	(select genre_name from dbo.genres g       where g.genre_id = ag.genre_id)   as 'genre'
from dbo.movies m
join dbo.associated_writers aw
  on m.movie_id = aw.movie_id
join dbo.associated_actors aa
  on m.movie_id = aa.movie_id
join dbo.associated_genres ag
  on m.movie_id = ag.movie_id;


-- not null constraint check using insert/update statements
-- the following not null checks should ALL FAIL
insert into dbo.directors values (107, NULL);
insert into dbo.writers   values (107, NULL);
insert into dbo.actors    values (107, NULL);
insert into dbo.genres    values (107, NULL);

insert into dbo.movies values (107, 'movie TEST7', 3600, NULL, 'USA', 106);
insert into dbo.associated_writers values (106, NULL);
insert into dbo.associated_writers values (NULL, 103);
insert into dbo.associated_actors  values (NULL, 101);
insert into dbo.associated_actors  values (102, NULL);
insert into dbo.associated_genres  values (103, NULL);

insert into dbo.revenues values (107, 101, NULL, 32000000.75, 576002.15, 75649.00);
insert into dbo.revenues values (108, 101, 13000000.50, NULL, 576002.15, 75649.00);
insert into dbo.revenues values (109, 101, 13000000.50, 32000000.75, NULL, 75649.00);
insert into dbo.awards   values (NULL, 'best actor', NULL);
insert into dbo.awards   values (NULL, NULL, 'oscar');
insert into dbo.ratings  values (107, NULL, 8, 101);
insert into dbo.ratings  values (108, 'google', NULL, 101);
insert into dbo.ratings  values (109, 'amazon reviews', 7, NULL);


-- following associated tables inserts should FAIL, illegal movie_id PKs
insert into dbo.associated_writers values (121, 103);
insert into dbo.associated_writers values (120, 103);
insert into dbo.associated_actors  values (350, 101);
insert into dbo.associated_actors  values (999, 102);
insert into dbo.associated_genres  values (550, 102);


-- deleting all test records, database clean-up
delete from dbo.ratings;
delete from dbo.awards;
delete from dbo.revenues;
delete from dbo.associated_genres;
delete from dbo.associated_actors;
delete from dbo.associated_writers;
delete from dbo.movies;
delete from dbo.genres;
delete from dbo.actors;
delete from dbo.writers;
delete from dbo.directors;
