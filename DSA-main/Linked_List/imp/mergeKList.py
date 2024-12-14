class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def mergeKlist(arr, k):
    from queue import PriorityQueue
    pq = PriorityQueue()
    for i in range(k):
        if arr[i] is not None:
            pq.put((arr[i].data, i))
    head = Node(None)
    curr = head
    while not pq.empty():
        val, i = pq.get()
        curr.next = Node(val)
        curr = curr.next
        if arr[i].next is not None:
            pq.put((arr[i].next.data, i))
            arr[i] = arr[i].next
    return head.next


def printList(node):
    while node:
        print(node.data, end=' ')
        node = node.next

if __name__ == '__main__':
    k, n = 3, 4
    arr = [None] * k
    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = mergeKlist(arr, k)
    printList(head)