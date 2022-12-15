


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    nodeA = headA
    nodeB = headB
    while nodeB:
        while nodeA:
            if nodeB == nodeA:
                return nodeB
            nodeA = nodeA.next
        nodeA = headA
        nodeB = nodeB.next
    return None