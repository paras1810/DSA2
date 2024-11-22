def wordBreak(word, dicto):
    dp = [False for i in range(len(word)+1)]
    dp[0] = True
    for i in range(len(word)+1):
        for j in range(i):
            if dp[j] and word[j:i] in dicto:
                dp[i] = True
                break
    return dp[len(word)]



if __name__ == "__main__":
    dictionary = ["mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice",
                  "cream"]
    dicto = set()
    for i in dictionary:
        dicto.add(i)
    if (wordBreak("ilikesamsung", dicto)):
        print("Yes")
    else:
        print("No")

