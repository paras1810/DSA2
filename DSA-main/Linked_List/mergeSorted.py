class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def addToList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

def mergeLists(headA, headB):
    dummy_node = Node(0)
    tail = dummy_node
    while True:
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    return dummy_node.next

if __name__ == '__main__':
    listA = LinkedList()
    listB = LinkedList()
    listA.addToList(5)
    listA.addToList(10)
    listA.addToList(15)

    listB.addToList(2)
    listB.addToList(3)
    listB.addToList(20)

    listA.head = mergeLists(listA.head, listB.head)
    listA.printList()


