


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
    
    listA, listB = headA, headB
    while listA != listB:
        listA = listA.next if listA else headB
        listB = listB.next if listB else headA
    return listA

