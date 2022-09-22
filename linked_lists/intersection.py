


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        Lists are not necessarily the same length.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None

    ha = headA
    hb = headB

    while ha is not hb:
        # Move node of each list to next one
        # If it reaches the end and no match is found, point it to start of other linked list
        ha = headB if ha is None else ha.next
        hb = headA if hb is None else hb.next

    # If they instersect, either ha or hb point to the same node
    # If they don't intersect, ha or hb are at the end of the list and are None
    return ha


