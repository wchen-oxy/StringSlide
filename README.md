# StringSlide
Our final project centered around guitars for databases. Think wikipedia meets facebook. 


Requirements:
postgresql running in virtual environment
brew installed in virtual enviornment (used to launch postgresql)


postgresql instructions:
(https://stackoverflow.com/questions/7975556/how-to-start-postgresql-server-on-mac-os-x)

The Homebrew package manager includes launchctl plists to start automatically. For more information run brew info postgres.

Start manually:

pg_ctl -D /usr/local/var/postgres start

Stop manually:

pg_ctl -D /usr/local/var/postgres stop

Start automatically:

"To have launchd start postgresql now and restart at login:"

brew services start postgresql