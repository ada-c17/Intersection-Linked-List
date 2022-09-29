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

    while currA:
        while currB:
            if currA == currB:
                return currA
            currB = currB.next
        currB = headB
        currA = currA.next
    return None
