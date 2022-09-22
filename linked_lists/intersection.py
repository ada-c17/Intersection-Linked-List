

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
    else:
        currentA = headA
        currentB = headB
        nodes = set()
        while currentA.next:
            nodes.add(currentA)
            currentA = currentA.next

        while currentB.next:
            if currentB in nodes:
                return currentB
            currentB = currentB.next

    return None
