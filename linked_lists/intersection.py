


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    pointer_a = headA
    pointer_b = headB

    while pointer_a and pointer_b:
        if pointer_a == pointer_b:
            return pointer_a

        pointer_a = pointer_a.next 
        pointer_b = pointer_b.next 

        if pointer_a == pointer_b:
            return pointer_a
        if not pointer_a:
            pointer_a = headB
        if not pointer_b:
            pointer_b = headA    
    
    return None