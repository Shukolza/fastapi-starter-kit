from src.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    # you might change what's unique depending of what do you want to use as the first factor
    # if so, you'll also need to change a couple lines in:
    # services.user, schemas.user, api.auth and main, I also stated it there
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
