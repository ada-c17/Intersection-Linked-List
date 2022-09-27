


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    # return None immediately if one or both lists is empty
    if headA is None or headB is None:
        return None

    # create two pointers - one to traverse each list
    current_A = headA
    current_B = headB

    # Linked lists may have different lengths
    # If you finish traversing one list, switch head & start traversing other list
    # In other words, traverse (A + B) & (B + A)
    # Eventually current_A == current_B; either at intersect point or None if there is no intersect
    while current_A != current_B:
        current_A = headB if not current_A else current_A.next
        current_B = headA if not current_B else current_B.next
    return current_A
