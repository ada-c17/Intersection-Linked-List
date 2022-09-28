
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    # create new set to store all node
    visited = set()
    currentA, currentB = headA, headB

    # add all nodes in headA into visited set
    while currentA:
        visited.add(currentA)
        currentA = currentA.next

    # check headB in visited set, if it is in there then return the node that is intersection
    while currentB:
        if currentB in visited:
            return currentB
        currentB = currentB.next
    return None

