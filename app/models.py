from typing import Optional
from sqlmodel import Field, SQLModel


class CovidCaseBase(SQLModel):
    user_id: str


class CovidCase(CovidCaseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CovidCaseCreate(CovidCaseBase):
    pass


class CovidCaseRead(CovidCaseBase):
    id: int