from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///minilinks.db", echo=False, future=True)


class Base(DeclarativeBase):
    pass


class Url(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True)

    short_url: Mapped[str] = mapped_column(index=True, nullable=False, unique=True)
    original_url: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
