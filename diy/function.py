# This is new file that separate from main `app.py`
# Executeable only

def get_topics(request, response):

    response.text = "Test new function for separate files"

def new_topics(request, response):

    response.text = "Voila, it's worked!"