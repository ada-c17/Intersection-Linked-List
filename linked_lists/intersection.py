

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = headB if not p1 else p1.next
        p2 = headA if not p2 else p2.next
    return p1
