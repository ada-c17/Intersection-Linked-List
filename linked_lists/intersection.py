


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    visited = set()
    curA, curB = headA, headB
    while curA:
        visited.add(curA)
        curA = curA.next
    while curB:
        if curB in visited:
            return curB
        curB = curB.next
    return None