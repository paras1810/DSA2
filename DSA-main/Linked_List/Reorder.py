class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


    def reorderList(self):
        head = self.head
        if head == None or head.next == None:
            return
        n = 0
        walk = head
        while(walk):
            walk = walk.next
            n = n+1
        head2 = head
        for i in range((n-1)//2):
            head2 = head2.next
        tail = head2
        head2 = head2.next
        tail.next = None
        prv = None
        nex = head2.next
        while head2:
            nex = head2.next
            head2.next = prv
            prv = head2
            head2 = nex
        head2 = prv
        walk = head
        walk2 = head2
        while walk2:
            temp = walk.next
            walk.next = walk2
            walk = temp
            temp = walk2.next
            walk2.next = walk
            walk2 = temp

        if tail:
            tail = tail.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.printList()
    n = 2
    llist.reorderList()
    print()
    llist.printList()


