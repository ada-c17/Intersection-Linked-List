class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None 
    pointer1 = headA
    pointer2 = headB
    while pointer1 != pointer2:
        if pointer1:
            pointer1 = pointer1.next
        else:
            pointer1 = headB
        if pointer2:
            pointer2 = pointer2.next
        else:
            pointer2 = headA
    return pointer1

    # make a traverseA and traverseB varaible to store the current node.
    # if a and b are equal save interesect = a or b 
    # move onto the next node, if not equal, change intersect to none 
    # otherwise move onto next node etc.