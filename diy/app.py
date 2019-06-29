from api import (
    API, 
    RequestAPI, 
    UserRequest, 
    UserRequestHandler,
    UserRequestBasedHandler
)
app = UserRequestBasedHandler()

# Base example for routing

@app.route("/home")
def home(request, response):

    response.text = "Hello from home page"

@app.route("/about")
def about(request, response):

    response.text = "Hello from about page"

@app.route("/post/{topic}")
def topic(request, response, topic):

    response.text = f"This post is {topic}"

# example of new routing fo
# class-based handlers

@app.route("/new")
class NewTopics:
    def get(self, request, response):

        response.text = "This is new topic"

    def post(self, request, response):

        response.text = "Post new topic"

def handler(request, response):

    response.text = "test new route"

app.url("/index", handler)