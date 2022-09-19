class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    currentA = headA;
    while currentA != None:
        currentB = headB;
        while currentB != None:
            if currentA is currentB:
                return currentA
            currentB = currentB.next
        currentA = currentA.next
