


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    visited_nodes = set()

    while headA:
        visited_nodes.add(headA)
        headA = headA.next

    while headB:
        if headB in visited_nodes:
            return headB
        headB = headB.next

    return None

