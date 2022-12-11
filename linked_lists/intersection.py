


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None

    a = headA
    b = headB

    while a != b:
        if a:
            a = a.next
        else:
            a = headB
        if b:
            b = b.next
        else:
            b = headA
    return a