
def threeSum(arr):
    n = len(arr)
    arr.sort()
    for i in range(n-1, -1, -1):
        l, r = 0, i-1
        while l < r:
            if arr[i] == arr[l] + arr[r]:
                print(arr[i], arr[l], arr[r])
                break
            elif arr[i] > arr[l] + arr[r]:
                l += 1
            else:
                r -= 1



if __name__ == "__main__":
    arr = [3, 7, 9, 1, 12, 8, 10]
    # 3, 7, 10  :3 + 7 = 10
    # 7, 1, 8   : 7 + 1= 8
    # arr = [1, 3, 7, 8, 9, 10 ,12]
    threeSum(arr)

    #Time: O(n^2)
    #Space: O(1)