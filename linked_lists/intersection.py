


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    nodesA = set()
    curA = headA
    while curA:
        nodesA.add(curA)
        curA = curA.next
    curB = headB
    while curB:
        if curB in nodesA:
            return curB
        curB = curB.next
    return None