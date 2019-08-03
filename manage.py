# coding=utf-8

from app import task1
from app import task2

task1.add.delay(2, 4)
task2.multiply.delay(4, 5)

print("end...")
