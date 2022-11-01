


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    head_one = headA
    head_two = headB
    while head_one != head_two:
        if head_one:
            head_one = head_one.next
        else:
            head_one = headB
        if head_two:
            head_two = head_two.next
        else:
            head_two = headA
    return head_one


