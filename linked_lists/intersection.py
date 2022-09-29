


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
        linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
        linked_list_b: 1 -> 2 -> 5 -> 6 -> 7
    """
    if not headA or not headB:
        return None
    
    current_a, current_b = headA, headB
    intersection = None

    while current_a != current_b:
        current_a = headB if not current_a else current_a.next
        current_b = headA if not current_b else current_b.next
    intersection = current_a

    return intersection

