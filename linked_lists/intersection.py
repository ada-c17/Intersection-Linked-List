


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

    intersection = None
    pointer_a = headA
    pointer_b = headB

    while pointer_a and pointer_a.next:
        if pointer_b == pointer_a and intersection == None:
            intersection = pointer_a
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        elif pointer_a != pointer_b and intersection != None:
            return None
        elif pointer_a == pointer_b and intersection != None:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        elif pointer_b.next == None:
            pointer_a = pointer_a.next
            pointer_b = headB
        else:
            pointer_b = pointer_b.next

    return intersection
