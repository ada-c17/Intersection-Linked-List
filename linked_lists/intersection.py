


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currentA = headA

    while currentA:
        currentB = headB
        while currentB:
            if currentA == currentB:
                return currentA
            currentB = currentB.next
        currentA = currentA.next
    
    return None


