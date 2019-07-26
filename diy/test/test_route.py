import pytest

from diy.api import UserRequestBasedHandler


@pytest.fixture
def request_user_based_handler():
    """ 
    return UserRequestBasedHandler
    """

    return UserRequestBasedHandler()


def test_basic_route(request_user_based_handler):
    """
    test to handle route
    """

    @request_user_based_handler.route("/home")
    def home(request, response):

        response.text = "test from home route"

def test_exception_on_route(request_user_based_handler):

    """
    test to handle route 
    and throw exception
    """ 

    @request_user_based_handler.route("/home")
    def home(request, response):

        response.text = "test again from here"

        with pytest.raises(AssertionError):
            @request_user_based_handler.route("/home")
            def homepage(request, response):

                response.text = "test again from here"