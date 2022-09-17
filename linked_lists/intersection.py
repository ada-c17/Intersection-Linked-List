


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.

    """
    hashSet = set ()
    hA, hB = headA, headB


    if not hA or not hB:
        return None


    while hA: 
        hashSet.add(hA) 
        hA = hA.next

    while hB:
        if hB in hashSet:
            return hB
        hB = hB.next
    return None


