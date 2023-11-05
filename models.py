from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, func

from datetime import datetime


POSTGRES_DSN = f'postgresql://app:secret@127.0.0.1:5431/app'

engine = create_engine(POSTGRES_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Advertise(Base):

    __tablename__ = 'advertise'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=False, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    author: Mapped[str] = mapped_column(String(100), nullable=False)



Base.metadata.create_all(bind=engine)
# У объявления должны быть следующие поля:

#     заголовок
#     описание
#     дата создания
#     владелец




