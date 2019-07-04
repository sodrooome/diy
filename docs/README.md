---
home: true
actionText: Take Me There →
actionLink: /index/
features:
- title: Beginner Friendly
  details: Minimal setup to dive in Python web framework, no experience required
- title: Performant
  details: Run independently on WSGI server generates, no install dependencies
- title: Easy to Use
  details: Only uses fundamentals Python and HTML languages, zero configuration  
footer: BSD-3 Licensed | Copyright © Ryan Febriansayh
---

## Requirement

Python 3.6+

## Installation

for development and learning purposes you can clone the original repo
```bash
git clone https://github.com/sodrooome/diy.git
```

## Minimal Configuration

```python
from api import UserRequestHandler()

app = UserRequestHandler()

@app.route("/")
def home(req, resp):
    resp.text = "Hello, World!"
```

Save this file, and run with `gunicorn` (for Linux/Mac users)

```sh
gunicorn <your_file>:app
```

And voila! try to see what happens in your browser