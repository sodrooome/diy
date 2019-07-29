import pytest

from diy.api import UserRequestBasedHandler


@pytest.fixture
def user_request_based_handler():

    return UserRequestBasedHandler()


@pytest.fixture
def client(user_request_based_handler):

    return user_request_based_handler.session()
