import threading
def print_even(*args):
    print("List of Even Numbers")
    print(args)
    # for i in range(li):
    #     print(i, end=" ")

def odd_even(*args):
    print("List of Odd Numbers")
    print(args)
    # for i in range(li):
    #     print(i, end=" ")

if __name__ == "__main__":
    li = [23, 55, 12, 45]
    lo = li[0:2]
    le = li[2:4]
    print(lo, le)
    even_thread = threading.Thread(target=print_even, args=(lo))
    odd_thread = threading.Thread(target=odd_even, args=(le))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()


