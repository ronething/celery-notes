# coding=utf-8

import djcelery

djcelery.setup_loader()

CELERY_IMPORTS = (
    "course.tasks"
)

CELERY_QUEUES = {
    "beat_tasks": {
        "exchange": "beat_tasks",
        "exchange_type": "direct",
        "binding_key": "beat_tasks"
    },
    "work_queue":{
        "exchange": "work_queue",
        "exchange_type": "direct",
        "binding_key": "work_queue"
    }
}

CELERY_DEFAULT_QUEUE = "work_queue"

# 有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的 worker 数量
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个 worker 最多执行 100 个任务被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大执行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    "task1": {
        "task": "course-task",
        "schedule": timedelta(seconds=5),
        "options": {
            "queue": "beat_tasks",
        }
    },
}