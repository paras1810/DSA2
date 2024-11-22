
def closeGreat(arr):
    n = len(arr)
    st = [arr[0]]
    i = 0
    for j in range(1, n):
        while st and arr[j] > st[-1]:
            if arr[j] > st[-1]:
                print(arr[j], end=' ')
                st.pop()
        st.append(arr[j])
    while st:
        print(-1, end=' ')
        i = i-1
        st.pop()




if __name__ == "__main__":
    arr = [3, 7, 9, 1, 12, 8, 10]
    arr1 = [1, 7, 9, 5, 8, 11]
    closeGreat(arr1)

    #arr1 = [7, 9, 11, 8, 11, -1]

    # right big Closest
