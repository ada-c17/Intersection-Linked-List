


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    try: 
        if headB.next:
            headB_first = headB
        while headA.next:
            while headB.next:
                if headA == headB:
                    return headA
                else:
                    headB = headB.next
            else:
                headA = headA.next
                headB = headB_first
    except:
        return None
    