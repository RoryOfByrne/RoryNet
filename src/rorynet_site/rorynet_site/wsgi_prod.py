import os
import sys

sys.path.append('/home/rorybyrne/webapps/rorynet/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rorynet_site.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
