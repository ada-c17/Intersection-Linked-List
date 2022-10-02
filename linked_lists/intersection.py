


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None



def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """


    cur_A = headA
    cur_B = headB

    count  = 0
    while cur_A!=cur_B:
        if cur_A.next and cur_B.next:
            cur_A = cur_A.next
            cur_B = cur_B.next
            if cur_A==None:
                count+=1
                if count >1:
                    return None
                cur_A = headB
            if cur_B==None:
                cur_B = headA
            
    return cur_A
