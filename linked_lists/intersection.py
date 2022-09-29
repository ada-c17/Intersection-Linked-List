


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    currentA = headA
    currentB = headB

    if currentA is None or currentB is None: 
        return None

    while currentA != currentB:
        if currentA:
            currentA = currentA.next 
        else: 
            currentA = headB
        
        if currentB: 
            currentB = currentB.next
        else: 
            currentB = headA

    return currentA