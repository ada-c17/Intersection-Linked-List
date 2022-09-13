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

    listA = []
    listB = []
    currentA = headA
    currentB = headB

    while currentA:
        while currentB.next:
            if currentB.val == currentA.val:
                inter = currentB
                match = check_match(currentA, currentB)
                if match:  
                    return inter
                else: 
                    return None
            else:
                currentB = currentB.next
        currentA = currentA.next
        currentB = headB
    return None

def check_match(currentA, currentB):
    while currentA and currentB:
        if currentA.next == currentB.next:
            currentA = currentA.next
            currentB = currentB.next
            match= True
        else:
            match = False
            break
    return match