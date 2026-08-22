import os
from dotenv import load_dotenv;
from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.engine import make_url



load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


#--------------------------------------------------------------------------------------

DB_READONLY_USER=os.getenv("DB_READONLY_USER")
DB_READONLY_PASSWORD=os.getenv("DB_READONLY_PASSWORD")


readonly_url = make_url(database_url).set(
    username=DB_READONLY_USER,
    password=DB_READONLY_PASSWORD,
)

readonly_engine = create_engine(
    readonly_url,
    pool_pre_ping=True,

)

def get_readonly_engine():
    """
    Return the SQLAlchemy engine used exclusively
    for executing LLM-generated SQL.
    """

    return readonly_engine