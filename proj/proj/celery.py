#! /usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
app = Celery('proj', broker = 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))