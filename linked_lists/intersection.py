


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA:
        return None

    current_node_a = headA
    current_node_b = headB

    list_b_map = {}
    intersection_point = None

    while current_node_b:
        list_b_map[current_node_b] = current_node_b.next
        current_node_b = current_node_b.next

    current_node_b = headB

    while current_node_a and current_node_b:
        if current_node_a in list_b_map and not intersection_point:
            intersection_point = current_node_a
            current_node_b = list_b_map[current_node_a]
        elif current_node_a not in list_b_map:
            intersection_point = None
    
        current_node_a = current_node_a.next
    
    return intersection_point