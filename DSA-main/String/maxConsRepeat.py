
def maxRepeat(str):
    cou = 0
    res = str[0]
    cur_count = 1
    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            cur_count += 1
        else:
            cur_count = 1
        if cur_count > cou:
            cou = cur_count
            res = str[i]
    return res


if __name__ == "__main__":
    str = "aabbaacccde"
    print(maxRepeat(str))