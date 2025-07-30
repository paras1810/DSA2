print("Hello WOrld")

class A:
    def __init__(self, name):
        self.name=name
        self.__private_name="private"
        self._protected="protected"

    def __private(self):
        print("This method is provate")

    def _protected(self):
        print("This method is protecetd")

    def public(self):
        print(f"Name is {self.name}")

name="Paras"
a=A(name)
print(a.public)
# print(a.private)
# print(a.protected)

v= 'abcdefghi'
print(v[::-2])
#"bdfh"


my_list = [1,5,3,17,4,3,1,7,5,4]
list1=[]
for i in my_list:
    if i not in list1:
        list1.append(i)
print(list1)

with open('filename.txt', 'w') as file:
    file.write("Hello, this is line inside file.\n")
    