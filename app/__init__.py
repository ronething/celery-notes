# coding=utf-8

from celery import Celery

app = Celery('demo')

# load config
app.config_from_object('app.celeryconfig')
