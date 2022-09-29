


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if headA is None or headB is None:
        return None
    
    currentA = headA 
    currentB = headB
    while currentA is not None:
        while currentB is not None:
            if currentA.val == currentB.val:
                return currentA
            currentB = currentB.next
        currentA = currentA.next
        currentB = headB
    return None