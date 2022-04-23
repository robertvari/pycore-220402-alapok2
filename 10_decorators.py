import random, time


def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()

        # worker runs here!!
        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Process time: {end_time - start_time}")

        return result

    return wrapper


@timer
def worker1(name):
    print(f"Worker1 Started: {name}")
    time.sleep(random.randint(3, 10))
    print("Worker1 Stopped.")


@timer
def worker2():
    print("Worker2 Started")
    time.sleep(random.randint(3, 10))
    print("Worker2 Stopped.")


@timer
def worker3():
    print("Worker3 Started")
    time.sleep(random.randint(3, 10))
    print("Worker3 Stopped.")


worker1("Robert")