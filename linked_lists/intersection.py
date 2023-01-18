


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    #linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
    # linked_list_b: 1 -> 2 -> 5 -> 6 -> 7
    
    if not headA or not headB: 
        return None
    
    current_a = headA
    current_b = headB

    while current_b:
        while current_a: 
            if current_a == current_b:
                return current_a
            current_a = current_a.next
            
        current_a = headA
        current_b = current_b.next

    return None
            