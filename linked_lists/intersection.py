


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    currentA = headA
    currentB = headB 

    # nested while loops
    while currentA is not None:
        while currentB is not None: 
            if currentA is currentB: 
                return currentA

            currentB = currentB.next
        
        currentA = currentA.next        
        currentB = headB
    
    return None




