


from ctypes import pointer


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    dict = {}
    while headA:
        dict[headA] = 1
        headA = headA.next

    print(dict)

    while headB:
        if headB in dict:
            return headB
        else:
            headB=headB.next
    return None

    
