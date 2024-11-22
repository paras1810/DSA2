

def anagram(s, p):
    if len(s) != len(p):
        return 0
    hash_s = [0] * 256
    hash_p = [0] * 256

    for i in range(0, len(s)):
        hash_s[ord(s[i])] += 1
        hash_p[ord(p[i])] += 1

    for i in range(0, 256):
        if hash_p[i] != hash_s[i]:
            return 0
    return 1

if __name__ == '__main__':
    str1 = "gram"
    str2 = "armg"
    print(anagram(str1, str2))