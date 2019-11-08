import multiprocessing

def f(x):
    return x**2

input_array = [1,2,3,4]

result = [f(x) for x in input_array]

pool = multiprocessing.Pool(4)

result2 = pool.map(f, input_array)


print(result)
print(result2)
