


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currA = headA
    currB = headB
    setA = set()
    
    if not (headA or headB):
        return None

    while currA:
        setA.add(currA)
        currA = currA.next

    while currB:
        if currB in setA:
            return currB
        currB = currB.next
    
    return None