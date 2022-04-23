import random, time
from utilities.decorators import print_result, timer


@print_result
@timer
def worker1(name):
    print(f"Worker1 Started: {name}")
    time.sleep(random.randint(3, 10))
    print("Worker1 Stopped.")
    return "Hello!!!"


worker1("Robert")