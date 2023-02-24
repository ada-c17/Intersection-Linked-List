


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    
    a, b = headA, headB
    if not a or not b:
        return None

    while a!=b:
        a = headB if not a else a.next
        b = headA if not b else b.next
    return a  