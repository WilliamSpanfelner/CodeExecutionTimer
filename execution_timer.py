import time
current_time = time.time()
print(f"current_time: {current_time}")

def speed_calc_decorator(function):
    def bench_mark():
        start_time = time.time()
        print(f"start_time: {start_time}")
        function()
        finish_time = time.time()
        elapsed_time = finish_time - start_time
        print(f"{function.__name__} run speed {elapsed_time}s")
    return bench_mark

@speed_calc_decorator
def fast_function():
    for i in range(10_000_000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100_000_000):
        i * i

fast_function()
slow_function()