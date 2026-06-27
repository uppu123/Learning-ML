## factorial Calculations

import multiprocessing
import math
import sys
import time

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(1000000)

def compute_fact(num):
    result = math.factorial(num)
    print(f"Factorial of {num} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 700, 8000]
    st_time = time.time()

    # create a pool of workers processes
    with multiprocessing.Pool() as pool:
        result = pool.map(compute_fact, numbers)
    
    end_time = time.time()

    print(result)
    print(f"time taken : {end_time - st_time} sec")