


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        Lists are not necessarily the same length.
        If the two linked lists have no intersection at all, return None.
    """
    # create intersecting value, default to None
    inter_node = None
    currentA = headA
    currentB = headB
    # traverse through A
    while currentA:
        # traverse through B
        while currentB:
            # if they match:
            if currentA == currentB:
                # traverse through remainder of A and B at same time
                # make new pointer variables to not lose place of currentA and currentB
                inner_currentA = currentA
                inner_currentB = currentB
                while inner_currentA and inner_currentB:
                    if inner_currentA == inner_currentB and inter_node is None:
                        inter_node = inner_currentA
                        
                    elif inner_currentA != inner_currentB:
                        inter_node = None
                        break
                    inner_currentA = inner_currentA.next
                    inner_currentB = inner_currentB.next
                if inter_node:
                    return inter_node
            
            currentB = currentB.next
        currentA = currentA.next
        currentB = headB # Restart from B list
    return inter_node


# Solution if lists are the same length
    # # create intersecting value, default to None
    # intersect_node = None
    # currentA = headA
    # currentB = headB
    # # while loop: headA and headB are not None
    # while currentA != None and currentB != None:
    #     # if values are the same and intersecting is None: reset intersecting
    #     if currentA == currentB and intersect_node is None:
    #         intersect_node = currentA
    #     # else: intersecting = None
    #     elif currentA != currentB:
    #         intersect_node = None
    #     # move up headA and headB position
    #     currentA = currentA.next
    #     currentB = currentB.next

    # # return intersecting
    # return intersect_node