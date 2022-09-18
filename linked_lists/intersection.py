


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def get_node_count(head):
    count = 0
    while head:
        count +=1
        head = head.next
    return count

def advance_list_head(head, advance):
    for i in range(advance):
        head = head.next
    return head


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    intersect = None
    node_count_a = get_node_count(headA)
    node_count_b = get_node_count(headB)

    difference = node_count_a - node_count_b

    if difference > 0:
        headA = advance_list_head(headA, difference)
    if difference < 0: 
        headB = advance_list_head(headB, abs(difference))
        
    while headA and headB:
        if headA == headB and not intersect:
            intersect = headA
        elif headA != headB and intersect:
            intersect = None
        headA = headA.next
        headB = headB.next
    
    return intersect