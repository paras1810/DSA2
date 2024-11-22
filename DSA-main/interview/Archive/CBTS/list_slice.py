def list_slice(string):
    ans = string[10::10]
    return ans


if __name__ == "__main__":
    string =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ans = list_slice(string)

    print(ans)

# slicing[start:end:gap]

#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]