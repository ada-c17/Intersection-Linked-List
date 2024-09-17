


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    # the nodes before the intersection can have different lengths
    # brute force approach (check each item in headA and see if it exists in headB and return if it does)
    # head a might need a variable dependent on the size of the list

    if not headA or not headB:
        return None

    current_a = headA


    while current_a:
        current_b = headB
        while current_b:
            if current_a == current_b:
                return current_a
            else:
                current_b = current_b.next
        current_a = current_a.next
        
    return None