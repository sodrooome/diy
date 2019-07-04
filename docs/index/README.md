---
index = true
---

# Documentation

## Basic Routing

here it provides simple routing, inspired by a Flask it can look like this :

```python
@app.route("/homepage")
def home(request, response):
    response.text = "Hello, World!"
```

the `route` in the code above is a decorator that is quite passable. You can also give a params in that `route` decorator too!

```python
@app.route("/topic/{football}")
def topic(request, response, football):
    response.text = f"This topic is {football}"
```

## Alternative Routing <Badge text="beta" type="warn"/>

or, if you looking for trouble to routing like method above, you can use alternative way like this :

```python
def post(request, response):
    response.text = "Alternative route method"

# passing the post function here
app.route_url("/new", post)
```

:::tip
Some tricks here, you can separate the functions that will be routing by creating a new file such as `function.py`, then do the import in your main programs (like `main.py` or `app.py`), which will be called
:::

it is **highly recommended** to separate our functions that will be executed later, can be seen as the following example like this :

- assume you want to create a new function, then put it in a new file likes `function.py` or `views.py`. At this occasion, i'm using `func.py`

```python
# func.py

def new_topics(request, response):
    response.text = "What's new?"
```

- do import that file in new file, here's example name `urls.py`, you are freely to name it

```python
# urls.py

from api import UserRequestBasedHandler
from func import new_topics

# define your application
app = UserRequestBasedHandler()

# passing that function here
app.url("/topics", new_topics)
```

And it's working! 
this is more profitable in our web performance later and make it simpler rather than stacking it in one file.

## Class Based Handlers <Badge text="future" type="danger"/>

For the future, DIY framework will try to implement class based handlers like that already implemented in Django. In general, class based handlers allow users to be able to route a function and class simultaneously on a large scale, such as if you want to use the method likes `get()`, `post()`, `delete()`.

Here's a draft that i propose :

```python
app.route("/new")
class NewTopics:
    def post_topics(self, request, response):
        response.text = "Post for new topics"

    def get_topics(self, request, response):
        response.text = "Get endpoint for new topics"
```

this is one of the most suitable features, but it is predicted that it takes a lot of time considering that it's built very complex.

<Index/>