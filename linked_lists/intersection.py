


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    node_a = headA
    node_b = headB

    if not node_a or not node_b:
        return None

    while node_a != node_b:
        if not node_a:
            # this is to set node_a to the head of b if null
            node_a = headB 
        elif not node_b:
            node_b = headA
        else:
            # if not null then we set the value to the next 
            node_a = node_a.next
            node_b = node_b.next

    # will either return null or the node where they are equal   
    return node_a 
