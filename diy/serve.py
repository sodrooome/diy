"""
this is only for Windows user, since gunicorn not compatible with Windows.
Run in terminal with `python serve.py`
"""

from waitress import serve
import app

serve(app.app, host='127.0.0.1', port=8080)