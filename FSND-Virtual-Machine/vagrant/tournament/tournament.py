#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def protect():
    """protects against SQL injection"""
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players (%s);", (name,))
    conn.commit()
    conn.close()

def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from Matches;")
    conn.commit() 
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from Players;")
    conn.commit() 
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    query="""
    select count(*) from Players;
    """
    c.execute(query)
    a=c.fetchall() 
    conn.close()
    return a[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into Players (player_name) values (%s)",(name,))
    conn.commit() 
    conn.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    query = """
    create view standings as
    select Players.player_id,Players.player_name,
        (SELECT count(Matches.winner_id) FROM Matches where player_id = Matches.winner_id) AS winn,
        (SELECT count(Matches.match_id) FROM Matches where player_id = Matches.winner_id OR Players.player_id = Matches.loser_id) AS games
    from Players
    order by winn desc, games desc;

    select * from standings;

    """
    c.execute(query)
    a=c.fetchall()
    conn.close()
    return a

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner_id:  the id number of the player who won
      loser_id:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into Matches (winner_id,loser_id) values (%s,%s)",(winner,loser))
    conn.commit() 
    conn.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    
    a = playerStandings()
    pear=[]
    for i in range(0,len(a),2):
        j=(a[i][0],a[i][1],a[i+1][0],a[i+1][1])
        pear.append(j)
    return pear

