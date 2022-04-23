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
    while not job_queue.empty():
        my_job = job_queue.get()
        print(f"Working on {my_job}")
        time.sleep(random.randint(3, 10))
        job_queue.task_done()

worker()