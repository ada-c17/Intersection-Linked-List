


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
    
    current_item_a = headA
    
    while current_item_a:
        current_item_b = headB
        while current_item_b:
            if current_item_a == current_item_b:
                return current_item_a
            current_item_b = current_item_b.next
        current_item_a = current_item_a.next
    
    return None