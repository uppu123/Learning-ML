import threading as th
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for i in 'abcde':
        time.sleep(1)
        print(i)


t = time.time()

#create threads

t1 = th.Thread(target = print_numbers)
t2 = th.Thread(target = print_letters)


#start threads
t1.start()
t2.start()


#wait for threads to complete
t1.join()
t2.join()



finished_time = time.time() - t
print(finished_time)