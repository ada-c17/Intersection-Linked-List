


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    while headB:
        temp = headA
        while temp:
            if temp == headB:
                return headB
            temp = temp.next
        headB = headB.next
    
    return None