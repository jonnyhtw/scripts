import multiprocessing
import os
import time

input_array = [1,2,3,4]

def f(x):
    time.sleep(5)
    return x**2

pool = multiprocessing.Pool(int(os.environ.get('NPROC',1)))

result = pool.map(f, input_array)

print(result)
