from api import API, RequestAPI, UserRequest, UserRequestHandler
app = UserRequestHandler()

@app.route("/home")
def home(request, response):

    response.text = "Hello from home page"

@app.route("/about")
def about(request, response):

    response.text = "Hello from about page"

@app.route("/post/{topic}")
def topic(request, response, name):

    response.text = "This post is {topic}"