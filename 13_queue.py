import threading, random, time, queue
import os

# list of files
file_list = os.listdir(r"C:\Work\_PythonSuli\pycore-220402\photos")

# create job queue
job_queue = queue.Queue()

# fill up job queue
for f in file_list:
    job_queue.put(f)


def worker():
    for i in file_list:
        print(f"Working on {i}")
        time.sleep(random.randint(3, 10))

worker()