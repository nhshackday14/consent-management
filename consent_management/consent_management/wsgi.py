import sys
import site
from os.path import basename, dirname
from os import environ

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)


USER = "ubuntu"
PROJECT_NAME = "consent-management"
MAIN_DIR_NAME = "consent_management"

site_dir = '/home/%s/.virtualenvs/consent-management/lib/python2.7/site-packages' % USER
sys_dir = '/home/%s/%s/%s' % (USER, PROJECT_NAME, MAIN_DIR_NAME)

activate_this = '/home/ubuntu/.virtualenvs/consent-management/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

#site.addsitedir(site_dir)
sys.path.insert(0, "/home/ubuntu/consent-management/consent_management")
settings_module = basename(dirname(__file__)) + '.settings'



environ['DJANGO_SETTINGS_MODULE'] = 'consent_management.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()