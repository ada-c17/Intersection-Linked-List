class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

"""
linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
linked_list_b: 1 -> 2 -> 5 -> 6 -> 7

return 5

linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
linked_list_b: 1 -> 2 -> 5 -> 4 -> 3

return None

"""

def countList(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    length_a = countList(headA)
    length_b = countList(headB)
    difference = 0
    long = None
    short = None

    if length_a > length_b:
        long = headA
        short = headB
        difference = length_a - length_b

    else:
        long = headB
        short = headA
        difference = length_b - length_a

    for i in range(difference):
        long = long.next

    while long != short:
        long = long.next
        short = short.next
    
    return long 
    
