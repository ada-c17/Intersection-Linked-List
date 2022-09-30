class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if headA is None or headB is None:
        return None 

    first = headA
    second = headB
    while first.next or second.next:
        if first==second:
            return first

        if first.next == None:
            first = headA
        else: 
            first = first.next

        if second.next == None:
            second = headB
        else: 
            second = second.next

    return None