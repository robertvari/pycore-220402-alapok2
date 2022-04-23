import time, random, threading


def worker1():
    print(f"Worker1 Started")
    for i in range(10):
        print(f"Worker1 processing: {i}")
        time.sleep(random.randint(3, 10))
    print("Worker1 Stopped.")


def worker2():
    print(f"Worker2 Started")
    for i in range(10):
        print(f"Worker2 processing: {i}")
        time.sleep(random.randint(3, 10))
    print("Worker2 Stopped.")


def worker3():
    print(f"Worker3 Started")
    for i in range(10):
        print(f"Worker3 processing: {i}")
        time.sleep(random.randint(3, 10))
    print("Worker3 Stopped.")


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)

t1.start()
t2.start()
t3.start()