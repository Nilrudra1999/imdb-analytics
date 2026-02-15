/*****************************************************************************
	  IMDb Analytics project - script for moving database file location
------------------------------------------------------------------------------
Author: Nilrudra Mukhopadhyay
Email: nilrudram@gmail.com
------------------------------------------------------------------------------
The script performs the following actions on the existing database:
1. uses the master system to perform the enxt actions
2. sets database offline before file transfer and alters the filenames
3. sets database back online after the transfer is complete
*****************************************************************************/
use master
go

alter database imdb_analytics_database set offline
go

alter database imdb_analytics_database
modify file (
	name=imdb_analytics_database,
	filename='D:\SOFTWARE DEV STUFF\film success predictor\data\imdb_analytics_database.mdf'
)

alter database imdb_analytics_database
modify file (
	name=imdb_analytics_database_log,
	filename='D:\SOFTWARE DEV STUFF\film success predictor\data\imdb_analytics_database_log.ldf'
)

alter database imdb_analytics_database set online
go
