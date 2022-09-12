


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def check_length(head):
    head_length = 0

    while head:
        head_length += 1
        head = head.next
    
    return head_length

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None

    headA_length = check_length(headA)    
    headB_length = check_length(headB)    

    if headA_length > headB_length:
        move = headA_length - headB_length
        while move:
            headA = headA.next
            move -= 1
    elif headB_length > headA_length:
        move = headB_length - headA_length
        while move:
            headB = headB.next
            move -= 1
    
    node_intersection = []
    keep_going = True
    while keep_going:
        if headA != headB:
            headA = headA.next
            headB = headB.next
            node_intersection = []
        elif headA == headB:
            node_intersection.append(headA)
            keep_going = False
    
    if not node_intersection:
        return None
    return node_intersection[0]

    
