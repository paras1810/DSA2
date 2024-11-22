def capitalize_decorator(function):
    def wrapper(str1, str2):
        str3 = str1.capitalize()
        str4 = str2.capitalize()
        string_hello = function(str3, str4)
        return string_hello
    return wrapper

@capitalize_decorator
def say_hello(str1, str2):
    return "Hi" + str1+ "How are you" + str2
    
if __name__ == "__main__":
    print(say_hello('ppparas', 'jain'))