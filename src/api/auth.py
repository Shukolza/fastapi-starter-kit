from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.schemas.token import Token
from src.schemas.user import UserRegister, UserLogin, UserOut
from src.services.user import UserService, get_user_service
from src.core.exceptions import (
    UserAlreadyExistsError,
    AuthException,
)

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(
    new_user_data: UserRegister, user_service: UserService = Depends(get_user_service)
):
    try:
        return await user_service.register_user(new_user_data)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            # change 'email' to 'username' if you use it as the first factor
            detail="A user with such an email already exists",
        )


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service),
):
    login_data = UserLogin(
        # change 'email' to 'username' if you use it as the first factor
        email=form_data.username, # that's how OAuth2PasswordRequestForm does this.
        password=form_data.password,
    )

    try:
        return await user_service.authenticate_user(login_data)
    except AuthException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong username or password!",
        )
