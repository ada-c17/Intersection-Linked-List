


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    listA = []
    listB = []
    
    currA = headA
    currB = headB

    while currA:
        listA.append(currA)
        currA = currA.next
    while currB:
        listB.append(currB)
        currB = currB.next

    first_same_node = None
    for i in range(1,min(len(listA)+1, len(listB)+1)):
        if listA[-i] != listB[-i] and not first_same_node:
            return None
        elif listA[-i] != listB[-i]:
            return first_same_node
        else:
            first_same_node = listA[-i]
    return first_same_node
        