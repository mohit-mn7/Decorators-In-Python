import time

def timer(decorated_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        decorated_function(*args, **kwargs)
        total_time = time.time() - start_time
        print("Time required to execute " + decorated_function.__name__ + " function: ", total_time )
    return wrapper

@timer
def function_1():
    for _ in range(100000):
        pass
@timer
def function_2(sleep_duration):
    time.sleep(sleep_duration)
    for _ in range(100000):
        pass

function_1()
function_2(5)
