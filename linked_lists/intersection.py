


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    set_a = set()
    current_a = headA
    current_b = headB

    while current_a:
        set_a.add(current_a)
        current_a = current_a.next

    while current_b:
        if current_b in set_a:
            return current_b
        current_b = current_b.next

    return None