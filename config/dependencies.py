from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()

# Create the SQLAlchemy engine
engine = create_engine(os.getenv("DATABASE_URL"))

db = Session(bind=engine)
