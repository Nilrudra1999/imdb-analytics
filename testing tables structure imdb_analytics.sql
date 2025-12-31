/*****************************************************************************
		IMDb Analytics project - script for testing sql tables structure
------------------------------------------------------------------------------
Author: Nilrudra Mukhopadhyay
Email: nilrudram@gmail.com
------------------------------------------------------------------------------
The script executes the following in the same order as written below:

- insert & update single records into tables	(should be successful)
- insert & update multi-records into tables		(should be successful)
- check unique and not null constraints			(should fail)
- check primary and foregin key constraints		(should fail)
- delete all newly added records from tables
******************************************************************************/
use imdb_analytics;
go
