


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
    p1, p2 = headA, headB
    while p1.val!= p2.val:
        p1 = p1.next if p1.next else headB
        p2 = p2.next if p2.next else headA

    return p1