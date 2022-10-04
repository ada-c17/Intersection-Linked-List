
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
 
    setA = set()
    currA = headA
    currB = headB

    while currA:
        setA.add(currA)
        currA = currA.next

    while currB:
        if currB in setA:
            return currB
        else:
           currB = currB.next

    return None 