


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currentA = headA
    currentB = headB
    intersection = None

    while currentB is not None:
        if currentA is currentB:
            intersection = currentA
            break

        currentA = currentA.next
        if currentA is None:
            currentA = headA
            currentB = currentB.next
    
    if not intersection:
        return None

    return intersection