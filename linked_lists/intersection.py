


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    current_A = headA
    current_B = headB

    while current_A:
        while current_B:
            if current_A == current_B:
                return current_A
            else:
                current_B = current_B.next
        current_A = current_A.next
        current_B = headB        


    return None