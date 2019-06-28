from api import API, RequestAPI, UserRequest, UserRequestHandler
app = UserRequestHandler()

@app.route("/home")
def home(request, response):

    response.text = "Hello from home page"

@app.route("/about")
def about(request, response):

    response.text = "Hello from about page"

@app.route("/post/{topic}")
def topic(request, response, topic):

    response.text = f"This post is {topic}"

@app.route("/new")
class NewTopics:
    def get(self, request, response):

        response.text = "This is new topic"

# example of new routing

def handler(request, response):

    response.text = "test new route"

app.route_url("/test", handler)

def eject(request, response):

    response.text = "eject new test"

app.route_url("/eject", eject)