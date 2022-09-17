class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB: return None

    headA_set = set()

    listA = headA
    while listA:
        headA_set.add(listA)
        listA = listA.next 
    
    listB = headB
    while listB:
        if listB in headA_set:
            return listB 
        listB = listB.next
    
    return None 