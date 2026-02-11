class ServiceException(Exception):
    """
    Base class for service exceptions
    """

    pass


class UserAlreadyExistsError(ServiceException):
    """
    Raised by UserService when
    attempting to register a user
    with a first factor that's already
    present in the database
    """

    pass


class AuthException(ServiceException):
    """
    Base class for authentication exceptions
    """

    pass


class UserNotFoundError(AuthException):
    """
    Raised by UserService when
    attempting to authenticate a user
    but the first factor is not found in the database
    """

    pass


class InvalidPasswordError(AuthException):
    """
    Raised by UserService when
    attempting to authenticate a user
    but the password is invalid
    """

    pass
