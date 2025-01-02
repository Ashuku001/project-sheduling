from piccolo_conf import *  # noqa

DB = PostgresEngine(
    config={
        "database": "postgres", 
        "user": "ashukuezra",
        "password": "admin",
        "host": "localhost",
        "port": 5432,
    }
)
