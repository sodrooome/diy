import pytest

from . conftest import user_request_based_handler, client


def test_client(user_request_based_handler, client):
    """ 
    test for client so user
    can send request to adapter 
    """

    RESP_TEXT = "Test from here (client)"

    @user_request_based_handler.route("/home")
    def homepage(request, response):

        response.text = RESP_TEXT

    assert client.get("http://baseserver/home").text == RESP_TEXT


def test_param_route(user_request_based_handler, client):
    """ 
    test for param in route
    """

    @user_request_based_handler.route("/{name}")
    def get(request, response, name):

        response.text = f"hello from {name}"

    assert client.get("http://baseserver/home")
