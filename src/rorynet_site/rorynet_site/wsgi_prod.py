import os
import sys

# sys.path.append('/home/rorybyrne/webapps/rorynet/rorynet/src/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rorynet_site.settings_prod")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
