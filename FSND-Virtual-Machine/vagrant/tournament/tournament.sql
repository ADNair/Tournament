-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP TABLE IF EXISTS Matches CASCADE;
DROP TABLE IF EXISTS Players CASCADE;
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE Players(
	player_id serial PRIMARY KEY,
	player_name TEXT
);

CREATE TABLE Matches(
	player_id serial REFERENCES Players(player_id) ON DELETE CASCADE,
	player_name TEXT,
	winner INTEGER REFERENCES Players(player_id) ON DELETE CASCADE,
	loser INTEGER REFERENCES Players(player_id) ON DELETE CASCADE
	CHECK (winner <> loser)
);
	
