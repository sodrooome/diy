# Passing UserRequestBasedHandler class to route new function
# then do Import new class from `function.py`
# Define your application to be execute

from api import UserRequestBasedHandler
from function import get_topics, new_topics

urls = UserRequestBasedHandler()

urls.url("/board", get_topics)
urls.url("/board/new", new_topics)
