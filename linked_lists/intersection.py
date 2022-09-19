


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
    
    nodesA = set()
    currentA = headA
    
    while currentA:
        nodesA.add(currentA)
        currentA = currentA.next
    
    currentB = headB

    while currentB:
        # If currentB is in the set, that's the intersection
        if currentB in nodesA:
            return currentB
        currentB = currentB.next
    return None