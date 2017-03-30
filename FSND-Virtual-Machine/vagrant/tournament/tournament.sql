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
	player_id SERIAL PRIMARY KEY,
	player_name TEXT
);

CREATE TABLE Matches(
	match_id SERIAL PRIMARY KEY,
	winner_id INTEGER REFERENCES Players(player_id) ON DELETE CASCADE,
	loser_id INTEGER REFERENCES Players(player_id) ON DELETE CASCADE
	CHECK (winner_id <> loser_id)
);
	
