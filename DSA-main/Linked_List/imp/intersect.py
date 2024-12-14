class Node:
    def __init__(self, data): 
        self.next = None 
        self.value = data 

def get_intersect(head1, head2):
    visited = set()
    curr1 = head1
    while curr1 is not None:
        visited.add(curr1)
        curr1 = curr1.next
    curr2 = head2 
    while curr2 is not None:
        if curr2 in visited:
            return curr2 
        curr2 = curr2.next 
    return None

if __name__ == "__main__":
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(20)

    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)
    head2.next.next.next  = head1.next

    intersection_point = get_intersect(head1, head2)
    if intersection_point is None:
        print("No intersection point")
    else:
        print("Intersection Point", intersection_point.value)