class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    if headA == None or headB == None:
        return None

    headA_set = set()
    currentA = headA
    while currentA:
        headA_set.add(currentA)
        currentA = currentA.next
    
    currentB = headB
    while currentB:
        if currentB in headA_set:
            return currentB
        currentB = currentB.next
    
    return None