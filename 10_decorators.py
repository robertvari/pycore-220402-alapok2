import random, time


def timer(func):

    def wrapper(*args, **kwargs):
        print("timer called")
        start_time = time.time()

        # worker runs here!!
        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Process time: {end_time - start_time}")

        return result

    return wrapper


def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result  is: {result}")
        return result
    return wrapper


@print_result
@timer
def worker1(name):
    print(f"Worker1 Started: {name}")
    time.sleep(random.randint(3, 10))
    print("Worker1 Stopped.")
    return "Hello!!!"


worker1("Robert")