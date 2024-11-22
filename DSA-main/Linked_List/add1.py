import sys
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def newNode(data):
    return Node(data)

def reverseList(head):
    if not head:
        return
    else:
        curNode = head
        prevNode = head
        nextNode = head.next
        curNode.next = None
        while nextNode:
            curNode = nextNode
            nextNode = nextNode.next
            curNode.next = prevNode
            prevNode = curNode
        return curNode

def addOne(head):
    head = reverseList(head)
    k = head
    carry = 0
    prev = None
    head.data += 1
    while head and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next

    if carry > 0:
        prev.next = Node(carry)
    return reverseList(k)


def printList(head):
    if not head:
        return
    else:
        while head:
            print(head.data, end=' ')
            head = head.next


if __name__ == "__main__":
    head = newNode(1)
    head.next = newNode(9)
    head.next.next = newNode(9)
    head.next.next.next = newNode(9)

    printList(head)

    addOne(head)

    printList(head)