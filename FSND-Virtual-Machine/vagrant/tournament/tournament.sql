-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE Players(
	id serial primary key,
	name text,
);

CREATE TABLE Matches(
	id serial PRIMARY KEY,
	winner INTEGER,
	loser INTEGER
);
	
