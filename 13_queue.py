import threading, random, time, queue
import os

file_list = os.listdir(f"C:\Work\_PythonSuli\pycore-220402\photos")


def worker():
    for i in file_list:
        print(f"Working on {i}")
        time.sleep(random.randint(3, 10))

worker()