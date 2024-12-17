
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL Database URL (replace with your credentials)
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/fitness_tracking_fast_api"

# SQLAlchemy Engine and Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for Models
Base = declarative_base()
