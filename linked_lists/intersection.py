


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    # create two temp references that refer to the current node in each list
    # create a boolean variable that stores whether an intersection has been found. initialized to false.
    # create a reference to the first node in intersection 

    # iterate through both lists at the same time
    # compare the temps at each stage
    #   if they are equal and intersection bool is currently False, set intersection bool to True, and update reference to first node in intersection
    #   if they are equal and intersetion bool is True, continue.
    #   if they are not equal but reference to intersection node has a non-NULL value, reset it to None, and reset intersection bool to False

    # if loop exists and intersection values are nullish, return None, else, return the intersection node
    pass