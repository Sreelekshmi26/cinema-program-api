# django_celery/celery.py

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mymovies.settings")
app = Celery("mymovies")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
