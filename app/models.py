from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Url(Base):
    __tablename__ = "urls"

    id: Mapped[str] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(nullable=False)
