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

    temp1 = headA
    while temp1:
        headA_set.add(temp1)
        temp1 = temp1.next 
    
    temp2 = headB
    while temp2:
        if temp2 in headA_set:
            return temp2 
        temp2 = temp2.next
    
    return None 