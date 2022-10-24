


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    '''
    The algorithm is: Hashset
    1.Store all the elements of headA in a hashset
    2.Iterate through the headB and check for the first match and then return it.
    Time Complexity - O(n+m)
    Space Complexity - O(n)
    '''
    first_set = set()
    curr = headA

    while curr:
        first_set.add(curr)
        curr = curr.next

    curr = headB
    while curr:
        if curr in first_set:
            return curr
        curr = curr.next

    return None

