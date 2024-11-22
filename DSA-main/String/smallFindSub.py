
def findSubString(s, p):
    len1 = len(s)
    len2 = len(p)
    if len1 < len2:
        return "No"
    hash_p = [0] * 256
    hash_s = [0] * 256
    for i in range(0, len(p)):
        hash_p[ord(p[i])] += 1
    start, start_index, min_len = 0, -1, float('inf')
    count = 0
    for j in range(0, len1):
        hash_s[ord(s[j])] += 1
        if hash_p[ord(s[j])] >= hash_s[ord(s[j])]:
            count += 1
        if count == len2:
            while hash_s[ord(s[start])] > hash_p[ord(s[start])] or hash_p[ord(s[start])]==0:
                hash_s[ord(s[start])] -= 1
                start += 1
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start

    if start_index == -1:
        return "NO"
    return s[start_index:start_index+min_len]


if __name__ == "__main__":

    string = "this is a test string"
    pat = "tist"

    print(findSubString(string, pat))