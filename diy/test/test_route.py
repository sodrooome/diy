import pytest

from diy.api import UserRequestBasedHandler, UserRequestHandler


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


def test_alternative_route(request_user_based_handler):
    """ 
    test alternative route
    """

    def home(request, response):
        response.text = "test from alternative route"

    request_user_based_handler.url("/homepage", home)


def test_alternative_route_for_class_based_handlers(request_user_based_handler):
    """ 
    test class based handlers 
    """

    def post(request, response):

        response.text = "test from here"

    def get(request, response):

        response.text = "test from here too"

    request_user_based_handler.url("/post", post)
    request_user_based_handler.url("/get", get)


def test_exception_on_class_based_handlers(request_user_based_handler):
    """
    test class based handlers route
    and throw exception
    """

    def post(request, response):

        response.text = "test from here"

    def get(request, response):

        response.text = "test from here too"

    request_user_based_handler.url("/post", post)

    with pytest.raises(AssertionError):

        request_user_based_handler.url("/post", get)


def test_exception_on_alternative_route(request_user_based_handler):
    """ 
    test alternative route
    and throw exception
    """

    def home(request, response):

        response.text = "test from alternative route again"

    request_user_based_handler.url("/homepage", home)

    with pytest.raises(AssertionError):

        request_user_based_handler.url("/homepage", home)


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
