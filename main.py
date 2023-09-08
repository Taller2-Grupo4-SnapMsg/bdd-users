
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("postgresql://cwfvbvxl:jtsNDRjbVqGeBgYcYvxGps3LLlX_t-P5@berry.db.elephantsql.com:5432/cwfvbvxl")


def app():
    with engine.connect() as conn:
        stmt = text("select * from pg_database")
        #print(conn.execute(stmt).fetchall())


if __name__ == "__main__":
    app()

