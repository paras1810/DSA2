def reverseBits(n):
    rev = 0
    while n > 0:
        rev = rev << 1
        if (n & 1 == 1):
            rev = rev ^ 1
        n = n >> 1
    return rev



if __name__ == "__main__":
    n = 11
    print(reverseBits(n))