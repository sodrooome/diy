from webob import Request, Response
from parse import parse

class API:

    """
    this is just for examples
    to get reponse Hello World in web browser
    """

    def __call__(self, environ, start_response):

        response_body = b"Hello World!"
        status = "200 OK"
        start_response(status, headers=[])
        return iter([response_body])

class RequestAPI:

    """
    this is just for examples
    to get reponse Hello World in web browser
    """

    def __call__(self, environ, start_response):

        request = Request(environ)
        response = Response()
        response.text = "Hello, World!"
        return response(environ, start_response)

class UserRequest:

    def __call__(self, environ, start_response):

        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):

        """
        based on mozilla documentation
        """

        user = request.environ.get("HTTP_USER_AGENT", "No User Agent Found")
        response = Response()
        response.text = f"This is {user}"
        return response

class UserRequestHandler:

    def __init__(self):

        self.routes = {}

    def route_url(self, path, handler):

        assert path not in self.routes, "Routes Already Exists"

        self.routes[path] = handler

    def route(self, path):

        def wrapper(handler):
            self.route_url(path, handler)
            return handler
        return wrapper

    def __call__(self, environ, start_response):

        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def default_response(self, response):

        response.status_code = 404
        response.text = "Page Not Found."

    def handle_request(self, request):

        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response

    def class_based_request(self, request):

        """
        class based views such as Django
        but it's not working and still draft
        """

        response = Response()

        handler, kwargs = self.find_handler_request(request_path=request.path)

        if handler is not None:
            if inspect.isclass(handler):
                handler = getattr(handler(), request.method.lower(), None)
                if handler is None:
                    raise AttributeError("Method now allowed", request.method)
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response

    def find_handler(self, request_path):

        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None