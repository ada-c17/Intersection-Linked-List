
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if headA is None or headB is None:
        return None

# Use current values for the pointers:
    pointer_a, pointer_b = headA, headB
# Use a while loop that
    while pointer_a != pointer_b:
        pointer_a = headB if pointer_a is None else pointer_a.next
        pointer_b = headA if pointer_b is None else pointer_b.next

    return pointer_a
