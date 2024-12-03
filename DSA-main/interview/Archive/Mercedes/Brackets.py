def check_b(s):
    res = []
    i = 0
    while(i<len(s)):
        if s[i] == '(':
            res.append(s[i])
        else:
            if len(res)>0:
                res.pop()
            else:
                return False
        i = i+1
    if len(res) == 0:
        return True    

if __name__ == "__main__":
    str = "(())()()"
    print(check_b(str))