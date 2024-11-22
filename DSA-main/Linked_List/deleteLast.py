class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def deleteLast(head, x):
    temp = head
    ptr = None
    while temp!=None:
        if temp.data == x:
            ptr = temp
        temp = temp.next

    if ptr!=None and ptr.next == None:
        temp = head
        while temp.next != ptr:
            temp = temp.next
        temp.next = None

    if ptr!=None and ptr.next != None:
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next

    return head




def newNode(data):
    node = Node(data)
    node.next = None
    return node

def display(head):
    temp = head
    while (temp!=None):
        print(temp.data, '-->')
        temp = temp.next

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)
head.next.next.next.next.next = newNode(4)
head.next.next.next.next.next.next = newNode(4)
print("Created Linked list: ")
display(head)
head = deleteLast(head, 4)
print("List after deletion of 4: ")
display(head)