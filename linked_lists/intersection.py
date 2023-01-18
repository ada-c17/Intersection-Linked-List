


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def len_check(head):
    head_len = 0

    while head:
        head_len += 1
        head = head.next

    return head_len


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None

    headA_len = len_check(headA)
    headB_len = len_check(headB)

    if headA_len > headB_len:
        move = headA_len - headB_len
        while move:
            headA = headA.next
            move -= 1
    elif headB_len > headA_len:
        move = headB_len - headA_len
        while move:
            headB = headB.next
            move -= 1

    while headA:
        if headA != headB:
            headA = headA.next
            headB = headB.next
        elif headA == headB:
            node_intersection = headA
            return node_intersection

    return None