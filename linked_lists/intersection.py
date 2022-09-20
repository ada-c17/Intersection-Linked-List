


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        Lists are not necessarily the same length.
        If the two linked lists have no intersection at all, return None.
    """
    # brute force solution?
    intersection_at = None
    currentA = headA
    # traverse through A
    while currentA:
        currentB = headB
        # traverse through B
        while currentB:
            # if they match:
            if currentA == currentB:
                # traverse through remainder of A and B at same time
                # make new pointer variables to not lose place of currentA and currentB
                inner_currentA = currentA
                inner_currentB = currentB
                while inner_currentA and inner_currentB:
                    if inner_currentA == inner_currentB and intersection_at is None:
                        intersection_at = inner_currentA
                        
                    elif inner_currentA != inner_currentB:
                        intersection_at = None
                        break
                    # subsequent nodes match, increment to next node
                    inner_currentA = inner_currentA.next
                    inner_currentB = inner_currentB.next
                if intersection_at:
                    return intersection_at
            currentB = currentB.next
        currentA = currentA.next
    return intersection_at


