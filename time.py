#  Writr a function to count n and evaluate a=n*10 for all values import time
import time

def count(n):
    for i in range(0, n):
        a = n * 10
ns =[100000,234234,34345,345,344,345]
n=100000
# Measure the start time
start_time = time.time() * 1000000  # Convert to microseconds
print(f"Start time: {start_time} microseconds")

# Timing the first function call/execution
count(1000000)

# Measure the end time
end_time = time.time() * 1000000  # Convert to microseconds
print(f"End time after first call: {end_time} microseconds")

# Calculate and print the duration of the first function call
duration = end_time - start_time
print(f"Duration of first function call: {duration} microseconds")

# Measure the start time for the second function call
start_time = time.time() * 1000000  # Convert to microseconds

# Timing the second function call/execution
count(1000000)

# Measure the end time for the second function call
end_time = time.time() * 1000000  # Convert to microseconds
print(f"End time after second call: {end_time} microseconds")

# Calculate and print the duration of the second function call
duration = end_time - start_time
print(f"Duration of second function call: {duration} microseconds")
