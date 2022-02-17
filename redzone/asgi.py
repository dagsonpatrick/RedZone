"""
ASGI config for redzone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import sys
import django
from channels.routing import get_default_application

sys.path.append('D:/IDES-DEV/PycharmProjects/RedZone/redzone')
sys.path.append('D:/IDES-DEV/PycharmProjects/RedZone/venv/Lib/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redzone.settings')

django.setup()

application = get_default_application()
