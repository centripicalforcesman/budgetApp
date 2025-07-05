# budgetApp

This project has 2 goals right now.

1. To build a budget app that my family can actually use, with the possible goal of releasing publicly if I get it up to a standard I am happy with.
2. To use different technologies than what I use in my day job as a learning exercise.  This list may grow, but right now, I plan on working with the following:
    - Python for backend
    - Postgres for database
       - SqlAlchemy, Alembic for ORM, and code first schema migrations
    - Angular for frontend
    - MongoDB. possibly for quicker reporting on past months, or a templating system to quickly generate budgets
    - Redis for serverside caching to save on some database calls
    - Will likely deplpy to AWS.
    - Using Linux Mint as OS for dev.



## Notes:
Run flask app with `python -m flask run`

Unit tests are currently run with `python -m unittest discover tests`

Create alembic migrations with `alembic revision -m "<name_of_migration>"`

Plan to document this, but followed this youtube vid, to set up postgres, SqlAlchemy, and alembic: https://www.youtube.com/watch?v=i9RX03zFDHU&t=1424s


## TODO:
- set up server-side and ui unit tests