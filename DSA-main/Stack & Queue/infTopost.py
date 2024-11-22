def notGreater(i, array):
    try:
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        a = precedence[i]
        b = precedence[array[-1]]
        return True if a <= b else False
    except KeyError:
        return False

def infixToPostfix(exp):
    output = []
    array = []
    for i in exp:
        if i.isalpha():
            output.append(i)
        elif i == '(':
            array.append(i)
        elif i== ')':
            while len(array) > 0 and array[-1] != '(':
                a = array.pop()
                output.append(a)
            if len(array) > 0 and array[-1] != '(':
                return -1
            else:
                array.pop()
        else:
            while len(array) > 0 and notGreater(i, array):
                output.append(array.pop())
            array.append(i)

    while len(array) > 0:
        output.append(array.pop())
    for ch in output:
        print(ch, end="")

if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    infixToPostfix(exp)