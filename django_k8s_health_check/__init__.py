# -*- coding: utf-8 -*-
try:
    import django
except ImportError:
    django = None

if django and django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'django_k8s_health_check.apps.DjangoHealthCheck'

__version__ = '1.1.1'
