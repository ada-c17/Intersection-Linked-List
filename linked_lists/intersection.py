


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


# def intersection_node(headA, headB):
    # """ Will return the node at which the two lists intersect.
    #     If the two linked lists have no intersection at all, return None.
    # """
    # if not headA or not headB:
    #     return None

    # a_node = headA
    # b_node = headB

    # while a_node:
    #     while b_node:
    #         if a_node == b_node:
    #             return a_node
    #         b_node = b_node.next
    #     a_node = a_node.next
    #     b_node = headB
    
    # return None

def intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    a_node = headA
    b_node = headB
    a_nodes = set()

    while a_node:
        a_nodes.add(a_node)
        a_node = a_node.next
    
    while b_node:
        if b_node in a_nodes:
            return b_node
        b_node = b_node.next
    
    return None