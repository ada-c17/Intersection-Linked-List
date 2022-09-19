


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    while headA is not None:
        tmp = headB
        while tmp is not None:
            if tmp == headA:
                return headA
            tmp = tmp.next
        headA = headA.next
    return None
