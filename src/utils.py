from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine


train_data = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/logistic-regression-project-tutorial/main/bank-marketing-campaign-data.csv", sep=';')