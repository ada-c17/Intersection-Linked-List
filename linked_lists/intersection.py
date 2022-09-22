


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currentA = Node(headA)
    currentB = Node(headB)
    node = 0
    if not currentA or not currentB:
        return None
    while currentA:
        if currentA.val == currentB.val:
            return currentA.val
        newA = Node(headA)
        newB = Node(headB)
        
    return None 