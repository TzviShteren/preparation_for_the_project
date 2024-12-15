from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

engine = create_engine(os.environ['PSQL_URL'])

session_maker = sessionmaker(bind=engine)
