from fastapi.testclient import TestClient
from sqlmodel import Session, select

from .database import engine
from .main import app
from .models import CovidCase


def test_create_covid_case():
    client = TestClient(app)  #

    response = client.post(  #
        "/cases/", json={
            "user_id": "0720f0d6-0e82-4be5-98f0-72c2c9f229a6"
        }
    )

    assert response.status_code == 204

    with Session(engine) as session:
        statement = select(CovidCase).where(CovidCase.user_id == "0720f0d6-0e82-4be5-98f0-72c2c9f229a6")
        cases = session.exec(statement).all()
        assert len(cases) == 1
