/*****************************************************************************
      IMDb Analytics project - relational query script - movies data
------------------------------------------------------------------------------
Author: Nilrudra Mukhopadhyay
Email: nilrudram@gmail.com
------------------------------------------------------------------------------
This script searches for correlations between movies and related data such
as revnues, ratings, awards, country of origin, etc. expressing analytical 
questions as SQL queries.
*****************************************************************************/
use imdb_analytics_database;
go


-- following queries are displayed in descending order ----------------------------
-- what movies have the best runtime to budget ratio, and what are their opening weekend profits?
-- which genres of movies have performed the best over the past 10 years?
-- which countries have consistently had the most profitable movies over the past 10 years?
-- what is the ratio of budget to domestic and international profits separately over the past 10 years?


-- following queries don't have a specific order to them --------------------------
-- what are the ratings of movies that haven't won awards or nominations?
-- how many movies have each director, writer, and actor either created or partaken in respectively?
-- which genres have each movie been attributed to over the past 10 years? group by genres
