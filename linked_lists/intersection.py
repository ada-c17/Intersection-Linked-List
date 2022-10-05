class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    while headA is not None:
        tempB = headB
        while tempB is not None:
            if headA == tempB:
                return headA
            tempB = tempB.next
        headA = headA.next

