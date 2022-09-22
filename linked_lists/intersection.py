


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    def checking_lens(head):
        len = 0
        while head:
            len += 1
            head = head.next
        return len

    lenA = checking_lens(headA)
    lenB = checking_lens(headB)

    if not headA or not headB:
        return None

    if lenA > lenB:
        move = lenA - lenB
        while move:
            headA = headA.next
            move -= 1

    elif lenB > lenA:
        move = lenB - lenA
        while move:
            headB = headB.next
            move -= 1
    while headA:
        if headA != headB:
            headA = headA.next
            headB = headB.next
        else:
            return headA