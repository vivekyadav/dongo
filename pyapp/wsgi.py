import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangomongo.settings'
import djangomongo.django.core.handlers.wsgi

proj_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(proj_dir, 'djangomongo'))

djangoapplication = djangomongo.django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)
