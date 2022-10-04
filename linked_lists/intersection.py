


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    set_a = set()
    current_A = headA
    current_B = headB

    # creating a set to store all nodes from linked list A
    while current_A:
        set_a.add(current_A)
        current_A = current_A.next

    # checking for the first common node for list A & B
    while current_B:
        if current_B in set_a:
            return current_B
        current_B = current_B.next

    return None