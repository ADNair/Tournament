Hello! This program is project four of Udacity's Full Stack NanoDegree Program.
It is a Swiss styled tournament. 

What is a Swiss styled tournament?: A Swiss-system tournament is a non-eliminating tournament format which features a set number of rounds of competition, but considerably fewer than in a round-robin tournament. 
In a Swiss tournament, each competitor (team or individual) does not play every 

Download:
- Python (this version in particular): https://www.python.org/downloads/release/python-2713/

- VirtualBox: https://www.virtualbox.org/wiki/Downloads. 
NOTE: I am running windows 10 and I ran into issues when running the latest version of VirtualBox. 
In order to match up with the guest additions of the VM, I had to download V4.3.40 of VirtualBox. 
Again, this is for WINDOWS 10 USERS ONLY. It will probably work fine outside of windows 10... surprise, surprise.

- Vagrant: https://www.vagrantup.com/

Once you have downloaded these programs, you may now proceed to running the program. 

Instructions for running:

In GitBash, cd to Udacity prepared Vagrant directory
Launch VM by VirtualBox configured with Vagrant $vagrant up
Log into the VM $vagrant ssh
cd to tournament directory
$ psql
Enter \i connect tournament.sql
Quit by entering \q
To test the database, $ python tournament_test.py

Congrats, you've done it!