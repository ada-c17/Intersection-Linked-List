from multiprocessing.sharedctypes import Value

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    
    if not headA or not headB:
        return None

    stackA = []
    stackB = []

    pointerA = headA
    pointerB = headB
    intersection = None

    while pointerA:
        stackA.append(pointerA)
        pointerA = pointerA.next
    
    while pointerB:
        stackB.append(pointerB)
        pointerB = pointerB.next
    
    while stackA and stackB:
        currentNodeA = stackA.pop()
        currentNodeB = stackB.pop()
        if currentNodeA == currentNodeB:
            intersection = currentNodeA
        elif intersection and currentNodeA.val != currentNodeB.val:
            return intersection
    
    return intersection
