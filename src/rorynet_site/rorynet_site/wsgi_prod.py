import os
import sys

sys.path.append('/home/rorybyrne/webapps/rorynet/rorynet/src/rorynet_site')
os.environ['DJANGO_SETTINGS_MODULE'] = "rorynet_site.settings_prod"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
