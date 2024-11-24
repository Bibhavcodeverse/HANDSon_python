import time 

def count(n):
    for i in range(0, n):
        a = n * 10

n = 1000000

def wrapper(func, n):
    start_time = time.time() * 1000000  # Start time in microseconds
    func(n)  # Call the function
    end_time = time.time() * 1000000  # End time in microseconds
    print(f"\nn = {n}, Time to execute is {end_time - start_time} microseconds")

# Call the wrapper function
wrapper(count, n)
