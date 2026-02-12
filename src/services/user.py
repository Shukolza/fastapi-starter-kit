from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import src.utils.security as security
from src.models.user import UserModel
from src.schemas.user import UserRegister, UserLogin, UserOut
from src.schemas.token import Token
from src.api.deps import SessionDep
from src.core.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
    InvalidPasswordError,
)


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, new_user_data: UserRegister) -> UserOut:
        # change email for username if you use it as the first factor
        if await self.get_user_by_email(new_user_data.email) is not None:
            raise UserAlreadyExistsError("User with such an email already exists!")

        hashed_password = security.get_password_hash(new_user_data.password)

        new_user = UserModel(
            email=new_user_data.email,
            username=new_user_data.username,
            password_hash=hashed_password,
        )

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return UserOut(
            id=new_user.id,
            email=new_user.email,
            username=new_user.username,
        )

    async def authenticate_user(self, login_data: UserLogin) -> Token:
        """
        Authenticates user with given data,
        returns an auth token
        """
        user = await self.get_user_by_email(login_data.email)

        if user is None:
            raise UserNotFoundError(f"User with email {login_data.email} not found!")

        if not security.verify_password(login_data.password, user.password_hash):
            raise InvalidPasswordError(f"Wrong password!")

        return Token(
            access_token=security.create_jwt({"sub": str(user.id)}), token_type="bearer"
        )

    # change every 'email' to 'username' if you use it as the first factor
    async def get_user_by_email(self, email: str) -> UserModel | None:
        query = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(query)
        result = result.scalars().first()
        # this fetches the user or None

        return result


def get_user_service(db_session: SessionDep) -> UserService:
    return UserService(db_session)
