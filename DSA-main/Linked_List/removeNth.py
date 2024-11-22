class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def remove(self, n):
        start = Node(-1)
        start.next = self.head
        fastptr = start
        slowptr = start
        for i in range(n):
            fastptr = fastptr.next

        while fastptr.next:
            fastptr = fastptr.next
            slowptr = slowptr.next

        slowptr.next = slowptr.next.next
        return start.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.printList()
    n = 2
    llist.remove(n)
    print()
    llist.printList()

