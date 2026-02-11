import jwt
from src.core.config import settings
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(plain_password: str) -> str:
    return password_hash.hash(plain_password)


def create_jwt(data: dict) -> str:
    to_encode = data.copy()

    if settings.ACCESS_TOKEN_EXPIRE_MIN is not None:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MIN
        )
        to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
