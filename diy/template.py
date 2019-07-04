import os
from jinja2 import Environment, FileSystemLoader
from api import UserRequestBasedHandler


class HtmlTemplate:

    def __init__(self, templates_dirs='templates'):

        self.templates_env = Environment(
            loader=FileSystemLoader(os.path.abspath(templates_dirs)))

    def template(self, template_name, context=None):

        if context is None:
            context = {}

        return self.templates_env.get_template(template_name).render(**context)
