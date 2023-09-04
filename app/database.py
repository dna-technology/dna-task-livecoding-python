from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
