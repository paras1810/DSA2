def check(s):
    p = []
    for c in s:
        if c == '(':
            p.append(c)
        else:
            if len(p) == 0:
                return 0
            else:
                if p[-1] == '(':
                    p.pop()
                else:
                    return 0
    if len(p) > 0:
        return 0
    return 1

if __name__ == '__main__':
    str = "()(())()"
    print(check(str))