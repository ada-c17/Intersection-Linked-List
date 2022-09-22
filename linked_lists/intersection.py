


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    nodes = set()

    while headA:
        nodes.add(headA)
        headA = headA.next

    while headB:
        if headB in nodes:
            return headB
        headB = headB.next
    
    return None
