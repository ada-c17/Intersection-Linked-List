


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currentA =  headA
    currentB = headB
    
    while currentA != currentB:
        if currentA is not None:
            currentA = currentA.next
        else:
            currentA = headB
        if currentB is not None:
            currentB = currentB.next
        else:
            currentB = headA

    return currentA