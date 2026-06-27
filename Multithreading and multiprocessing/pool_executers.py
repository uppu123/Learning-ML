## echniques to implement multithreading and multiprocessing in python





# Multithreading with thread pool executer

# from concurrent.futures import ThreadPoolExecutor
# import time

# def print_numbers(num):
#     time.sleep(2)
#     print(f"number : {num}")

# numbers = [1, 2, 3, 4, 5, 6, 7]

# t = time.time()

# with ThreadPoolExecutor(max_workers = 3) as executor:
#     results = executor.map(print_numbers, numbers)


# finished_time = time.time() - t
# print(finished_time)


## multiprecessing with process pool executor
from concurrent.futures import ProcessPoolExecutor
import time

def sq_numbers(num):
    time.sleep(2)
    print(f"number : {num*num}")

numbers = [1, 2, 3, 4, 5, 6, 7]

if __name__ == "__main__":
    t = time.time()

    with ProcessPoolExecutor(max_workers = 3) as executor:
        results = executor.map(sq_numbers, numbers)


    finished_time = time.time() - t
    print(finished_time)