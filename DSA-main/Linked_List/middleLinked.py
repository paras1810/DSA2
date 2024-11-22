class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next


    def printMiddle(self):
        count = 0
        mid = self.head
        heads = self.head
        while heads != None:
            if count & 1:
                mid = mid.next
            heads = heads.next

        if mid != None:
            print("Middle is ", mid.data)




if __name__ == "__main__":
    llist = LinkedList()
    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()

