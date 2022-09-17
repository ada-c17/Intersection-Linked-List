


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):

    hash_map = {}

    if not headA or not headB:
        return None

    while headA:
        hash_map[headA] = 1
        tailA = headA
        headA = headA.next

    while headB:
        if headB in hash_map.keys():
            intersection = headB
            while headB:
                tailB = headB
                headB = headB.next
            if tailB == tailA:
                return intersection
        headB = headB.next
    
    return None

    



