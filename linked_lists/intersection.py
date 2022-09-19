


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    list1, list2 = headA, headB

    while list1 != list2:
        list1 = list1.next if list1 else headB
        list2 = list2.next if list2 else headA

    return list1