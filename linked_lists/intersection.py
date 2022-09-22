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

    node_dict = {}

    a = headA
    b = headB

    while a.next:
        node_dict[a] = a.next
        a = a.next

    while b:
        if b in node_dict:
            if b.next == node_dict[b]:
                return b
        b = b.next

    return None