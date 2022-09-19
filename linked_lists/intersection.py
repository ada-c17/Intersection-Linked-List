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
    
    nodes_in_LL_A = set()
    curr_A = headA
    while curr_A:
        nodes_in_LL_A.add(curr_A)
        curr_A = curr_A.next

    curr_B = headB
    while curr_B:
        if curr_B in nodes_in_LL_A:
            return curr_B
        curr_B = curr_B.next
    
    return None