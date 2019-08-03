# coding=utf-8

from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = "redis://127.0.0.1:6379/1"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_IMPORTS = (
    "app.task1",
    "app.task2",
)

CELERYBEAT_SCHEDULE = {
    "task1": {
        "task": "app.task1.add",
        "schedule": timedelta(seconds=10),
        "args": (2,8)
    },
    "task2": {
        "task": "app.task2.multiply",
        "schedule": crontab(hour=17,minute=10),
        "args": (4,5)
    }
}