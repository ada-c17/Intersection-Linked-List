


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

    while currentB:
        while currentA:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
        currentA = headA
        currentB = currentB.next
    
    if currentA == currentB:
        return currentA
    
    return None

