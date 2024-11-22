
def deleteMid(st):
    n = len(st)
    temp = []
    count = 0
    while count < n/2-1:
        c = st[0]
        st.pop(0)
        temp.insert(0, c)
        count = count + 1
    st.pop(0)
    while len(temp) != 0:
        st.insert(0, temp.pop(0))



if __name__ == '__main__':
    st = []

    # insert elements into the stack
    st.insert(0, 1)
    st.insert(0, 2)
    st.insert(0, 3)
    st.insert(0, 4)
    st.insert(0, 5)
    st.insert(0, 6)
    st.insert(0, 7)
    deleteMid(st)

    # Printing stack after deletion of middle.
    while (len(st) != 0):
        p = st[0]
        st.pop(0)
        print(p, " ")