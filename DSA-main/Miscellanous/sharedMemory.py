from multiprocessing.shared_memory import SharedMemory
from multiprocessing import Process


# task executed in a child process
def task(shared_mem):
    # write some string data to the shared memory
    shared_mem.buf[:24] = b'Hello from child process'
    # close as no longer needed
    shared_mem.close()


# protect the entry point
if __name__ == '__main__':
    # create a shared memory
    shared_mem = SharedMemory(create=True, size=100)
    # create a child process
    process = Process(target=task, args=(shared_mem,))
    # start the child process
    process.start()
    # wait for the child process to finish
    process.join()
    # report the shared memory
    data = bytes(shared_mem.buf[:24]).decode()
    print(data)
    # close the shared memory
    shared_mem.close()
    # release the shared memory
    shared_mem.unlink()