


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
    
    currentA = headA
    currentB = headB
    intersect = None

    while currentA:
    
        if currentA == currentB:
            intersect = currentA
        else:
            currentB = currentB.next
        currentA = currentA.next
        
    return intersect