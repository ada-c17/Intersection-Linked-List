


from email.quoprimime import header_decode


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if headA is None or headB is None:
        return None

    currentA = headA
    currentB = headB

    while currentA is not currentB:
        if currentA == None:
            currentA = headB
            continue
        if currentB == None:
            currentB = headA
            continue
        currentA = currentA.next
        currentB = currentB.next

    return currentA