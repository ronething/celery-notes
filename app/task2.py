# coding=utf-8

import time
from app import app


@app.task
def multiply(x, y):
    time.sleep(3)
    return x * y
