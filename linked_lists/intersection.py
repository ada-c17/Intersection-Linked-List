


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    # traverse list and put items in an array
    seen = []
    current = headA
    while current is not None:
        seen.append(current)
        current = current.next

    # if item is in the set, you return the item
    current = headB
    while current is not None:
        if current in seen: 
            return current 

        current = current.next

    