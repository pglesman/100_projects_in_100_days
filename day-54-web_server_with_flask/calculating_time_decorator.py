import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapped_function(*args, **kwargs):
        before_func = time.time()
        result = function(*args, **kwargs)
        after_func = time.time()
        print(f'{function.__name__} run speed: {after_func - before_func}s')
        return result

    return wrapped_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
