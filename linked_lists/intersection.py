

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
        linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
        linked_list_b: 1 -> 2 -> 5 -> 6 -> 7
        return 5

        linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
        linked_list_b: 1 -> 2 -> 5 -> 4 -> 3
        return None

        note: should compare node not val for object equality
    """

    # O(n+m) time complexity and O(1) space complexity
    if headA is None or headB is None:
        return None

    la, lb = headA, headB
    # in worst case when length differ, after 1st traverse,
    # pointers point to the other head and traverse 2nd time
    while la != lb:
        if la:
            la = la.next
        else:
            la = headB
        if lb:
            lb = lb.next
        else:
            lb = headA
    return la
