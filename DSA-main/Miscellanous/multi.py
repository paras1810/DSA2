import threading 
import time 

def print_numbers():
    for i in range(5):
        print(f"Thread {threading.current_thread().name}->{i}")
        time.sleep(1)
    
thread1 = threading.Thread(target=print_numbers, name='A')
thread2 = threading.Thread(target=print_numbers, name='B')
thread1.start()
thread2.start()
thread1.join()
thread2.join()

import multiprocessing as mp

def print_numbers2():
    for i in range(5):
        print(f"Process {mp.current_process().name}->{i}")
        time.sleep(1)

process1= mp.Process(target=print_numbers2, name='A')
process2= mp.Process(target=print_numbers2, name='B')
process1.start()
process2.start()
process1.join()
process2.join()

import concurrent.futures as cf
import os

def task(name):
    for i in range(3):
        print(f"[{name}] Thread iteration {i}")
        time.sleep(1)
    return f"{name} done"

with cf.ThreadPoolExecutor(max_workers=2) as exc:
    futures = [
        exc.submit(task, "ThreadA"),
        exc.submit(task, "ThreadB")
    ]
    for future in cf.as_completed(futures):
        print(future.result())

def task2(name):
    for i in range(3):
        print(f"[{name}] Process iteration {i} (PID: {os.getpid()})")
        time.sleep(1)
    return f"{name} done"

if __name__ == "__main__":
    with cf.ProcessPoolExecutor(max_workers=2) as exc:
        futures=[
            exc.submit(task2, "Process A"),
            exc.submit(task2, "Process B")
        ]
        for future in cf.as_completed(futures):
            print(future.result())

# Asyncio: Efficient for high-concurrency I/O
# Joblib: Parallel in scientific computing
# Dask: Advanced parallelism with task graphs
# Celery: Distributed Task Queue


