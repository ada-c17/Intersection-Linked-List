

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

    nodeA, nodeB = headA, headB
    setA = set()
    while nodeA:
        setA.add(nodeA)
        nodeA = nodeA.next

    while nodeB:
        if nodeB in setA:
            return nodeB
        nodeB = nodeB.next
    return None
