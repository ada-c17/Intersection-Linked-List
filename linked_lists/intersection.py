


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not (headA and headB): #if one or both lists are empty return None
        return None
    curr1 = headA
    curr2 = headB
    start = None # the node where intersection begins
    seen = set() # to keep track of nodes that we have already seen
    while curr1.next or curr2.next:
        if curr1 == curr2 and not start: #if a match is found assign that to start
            start = curr1
        elif (curr1 != curr2) and start: #if mismatched nodes are found after start is assigned clear it
            start = None

        #if the node is in seen that means we found in it in the other list at a different position
        #assign that as start and travel through the lists to see if they are equal
        if curr1 in seen and not start:
            start = curr1
            curr2 = start
        elif curr2 in seen and not start:
            start = curr2
            curr1 = start
        elif curr1 != curr2 and not start:
            seen.add(curr1)
            seen.add(curr2)

        if curr1:
            curr1 = curr1.next
        if curr2:
            curr2 = curr2.next
    return start