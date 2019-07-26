import pytest

from diy.api import API, RequestAPI, UserRequest, UserRequestHandler, UserRequestBasedHandler

""" 
test to create a fixture
so we can pass every test
later
"""


@pytest.fixture
def api():
    """
    return API class that
    can use in every unit test
    """

    return API()


@pytest.fixture
def request_api():
    """
    return RequestAPI class
    """

    return RequestAPI()


@pytest.fixture
def request_user_handler():
    """
    return UserRequestHandler class
    """

    return UserRequestHandler()


@pytest.fixture
def request_user_based_handler():
    """ 
    return UserRequestBasedHandler
    """

    return UserRequestBasedHandler()
