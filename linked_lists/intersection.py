


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def find_length(head):
    length = 0
    current = head

    while current:
        length += 1
        current = current.next
    return length

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None

    headA_length = find_length(headA)
    headB_length = find_length(headB)

    # find the difference
    # if headA is longer
    if headA_length > headB_length:
        long_list = headA
        short_list = headB
        difference = headA_length - headB_length
    # if headB is longer
    else:
        long_list = headB
        short_list = headA
        difference = headB_length - headA_length

    # move the starting pointer of the longest list  
    for i in range(difference):
        long_list = long_list.next

    # loops goes on when the head doesn't match
    while long_list != short_list:
        long_list = long_list.next
        short_list = short_list.next

    return long_list


