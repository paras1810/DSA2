from concurrent.futures import ThreadPoolExecutor
from time import sleep
import logging

values = [3,4,5,6]

def cube(X):
    print("Cube", X*X*X)

if __name__ == "__main__":
    result = []
    with ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(cube,2)
        result = exe.map(cube,values)
        logging.error("GFG")

    for r in result:
        print(r)

