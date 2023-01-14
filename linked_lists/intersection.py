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

    nodeA = headA
    nodeB = headB
    while nodeA is not nodeB:
        nodeA = headB if nodeA is None else nodeA.next
        nodeB = headA if nodeB is None else nodeB.next 
    return nodeA
