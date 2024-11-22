def isPalindrome(s):
    s1 = s.replace(' ', '')
    s1 = s1.lower()
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False


s = "Too hot to hoot"
print(isPalindrome(s))