
def printNGE(arr):
    s = []
    element = 0
    next = 0
    s.append(arr[0])
    for i in range(1,len(arr)):
        next = arr[i]
        if len(s) != 0:
            element = s.pop()
            while element<next:
                print(str(element)+'--'+str(next))
                if len(s)==0:
                    break
                element = s.pop()
            if element>next:
                s.append(element)
        s.append(next)
    while len(s)>0:
        element=s.pop()
        next=-1
        print(str(element)+'--'+str(next))



if __name__ == "__main__":
    arr = [11, 13, 21, 3]
    printNGE(arr)