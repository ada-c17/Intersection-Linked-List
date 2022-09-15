


class Node:
    def __init__(self, value, next=None, previous=None):
        self.val = value
        self.next = next


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    if not headA or not headB:
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
        
    

    

    
    
    
    
    