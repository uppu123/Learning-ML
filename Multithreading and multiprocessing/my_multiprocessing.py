import multiprocessing as mp
import time


def sq_num():
    for i in range(5):
        time.sleep(1)
        print(f"squares : {i * i}")


def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"cubes : {i * i * i}")

if __name__ == "__main__":
    t = time.time()

    # create processes
    p1 = mp.Process(target = sq_num)
    p2 = mp.Process(target = cube_num)


    # start processes
    p1.start()
    p2.start()

    # wait for processes to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)