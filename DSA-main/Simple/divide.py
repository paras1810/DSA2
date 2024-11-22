def divide(a, b):
    try:
        c = a/b
        print(c)
    except Exception as e:
        return ("Divide")
    finally:
        return ("Finally")

if __name__ == "__main__":
    print(divide(18, 9))
