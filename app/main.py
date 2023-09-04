from typing import List

from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from .database import create_db_and_tables, engine
from .models import CovidCase, CovidCaseRead

app = FastAPI()

create_db_and_tables()


@app.get("/cases/", response_model=List[CovidCaseRead])
def read_cases():
    with Session(engine) as session:
        covid_cases = session.exec(select(CovidCase)).all()
        return covid_cases


@app.post("/cases/", status_code=204)
def create_case(*, covid_case: CovidCase):
    db_covid_case = CovidCase.from_orm(covid_case)
    with Session(engine) as session:
        session.add(db_covid_case)
        session.commit()
