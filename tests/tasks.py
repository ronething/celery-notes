# coding=utf-8

import time

from celery import Celery

broker = "redis://127.0.0.1:6379/1"
backend = "redis://127.0.0.1:6379/2"
app = Celery("mytask",broker=broker,backend=backend)

@app.task
def add(x,y):
    print ("enter call func...")
    time.sleep(3)
    return x+y