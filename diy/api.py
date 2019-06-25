from webob import Request, Response

class API:

    def __call__(self, environ, start_response):

        response_body = b"Hello World!"
        status = "200 OK"
        start_response(status, headers=[])
        return iter([response_body])

class RequestAPI:

    def __call__(self, environ, start_response):

        request = Request(environ)
        response = Response()
        response.text = "Hello, World!"
        return response(environ, start_response)