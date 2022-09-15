


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

    current_a = headA
    
    while current_a:
        current_b = headB
        while current_b:
            if current_a == current_b:
                return current_a
            current_b = current_b.next
        current_a = current_a.next
    
    return None