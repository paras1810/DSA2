from concurrent.futures import ThreadPoolExecutor

def cube(n):
    print(n*n)

if __name__ == "__main__":
    str = "paras is jain"
    str1 = str.split(' ')
    print(str1)
    str2 = "#".join(str1)
    print(str2)
    li = [4,5,6,7]
    with ThreadPoolExecutor(max_workers=5) as ex:
        ex.submit(cube, 2)
        result = ex.map(cube,li)
    for r in result:
        print(r)


