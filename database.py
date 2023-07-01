import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import APICall

from dotenv import load_dotenv

load_dotenv()


db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")


engine = create_engine(
    f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def save_api_call(endpoint, params, result):
    """
    Saves an API call to the database.

    Args:
        endpoint (str): The API endpoint that was called.
        params (str): The parameters passed to the API call.
        result (str): The result of the API call.

    Returns:
        None
    """
    params_json = params.dict() if params else None
    session = Session()
    api_call = APICall(endpoint=endpoint,
                       params=params_json, result=result)
    session.add(api_call)
    session.commit()
    session.close()
