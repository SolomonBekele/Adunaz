<<<<<<< HEAD
"""
WSGI config for Adunaz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Adunaz.settings')

application = get_wsgi_application()
=======
"""
WSGI config for Adunaz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Adunaz.settings')

application = get_wsgi_application()
>>>>>>> a2e0f1685e363926ddf5be284c1ca01ebbbc7275
