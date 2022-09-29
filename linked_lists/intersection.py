


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

    a_current = headA
    b_current = headB
    intersection = None
    intersecting = False
    nodes_a = {}

    while a_current:
        nodes_a[a_current] = True
        a_current = a_current.next

    print(nodes_a)

    while b_current:
        if nodes_a.get(b_current):
            
            if not intersecting:
                intersection = b_current
            intersecting = True

        else: intersecting = False
        b_current = b_current.next
        
    if intersecting:
        return intersection
    else:
        return None
