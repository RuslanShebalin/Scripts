import time


def timeit(func):
    def time_work(*args, **kwargs):
        ts = time.perf_counter()
        result = func(*args, **kwargs)
        te = time.perf_counter()
        td = (te-ts) * 1000  # time in ms
        print(f'Execution time: {td:.5f}ms')
        return result

    return time_work
