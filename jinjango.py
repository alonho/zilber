from django.http import HttpResponse
from django.conf import settings
from jinja2 import Environment, ChoiceLoader, FileSystemLoader
 
# Setup environment
default_mimetype = settings.DEFAULT_CONTENT_TYPE
 
# Create the Jinja2 Environment
env = Environment(loader=ChoiceLoader([FileSystemLoader(path) for path in settings.TEMPLATE_DIRS]))
 
def render_to_string(filename, context={}):
    return env.get_template(filename).render(**context)
 
def render_to_response(filename, context={},mimetype=default_mimetype, request = None):
    if request: context['request'] = request
    return HttpResponse(render_to_string(filename, context), mimetype=mimetype)
