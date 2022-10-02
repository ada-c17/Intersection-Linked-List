
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

    setA = set()

    currentA, currentB = headA, headB
    while currentA:
        setA.add(currentA)
        currentA = currentA.next

    while currentB:
        if currentB in setA:
            return currentB
        currentB = currentB.next
    
    return None