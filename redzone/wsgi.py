"""
WSGI config for redzone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('D:/IDES-DEV/PycharmProjects/RedZone/redzone')
sys.path.append('D:/IDES-DEV/PycharmProjects/RedZone/venv/Lib/site-packages')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redzone.settings')

application = get_wsgi_application()
