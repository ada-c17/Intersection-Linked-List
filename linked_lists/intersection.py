


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    a = headA
    b = headB
    while a != b:
        if not a:
            a = headB
        else:
            a = a.next

        if not b:
            b = headA
        else:
            b= b.next
    return a 