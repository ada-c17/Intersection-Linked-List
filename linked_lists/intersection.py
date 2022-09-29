


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    current_A = headA
    current_B = headB
    set_A = set()

    while current_A:
        set_A.add(current_A)
        current_A = current_A.next

    while current_B:
        if current_B in set_A:
            return current_B
        current_B = current_B.next

    return None

# Old solution: does not account for intersection in lists of differing lengths 
# def intersection_node(headA, headB):
#     """ Will return the node at which the two lists intersect.
#         If the two linked lists have no intersection at all, return None.
#     """
#     # create two temp references that refer to the current node in each list
#     current_A = headA
#     current_B = headB
#     # create a boolean variable that stores whether an intersection has been found. initialized to false.
#     intersection_found = False
#     # create a reference to the first node in intersection 
#     intersection_node = None

#     # iterate through both lists at the same time
#     # compare the temps at each stage
#     #   if they are equal and intersection bool is currently False, set intersection bool to True, and update reference to first node in intersection
#     #   if they are equal and intersetion bool is True, continue.
#     #   if they are not equal but reference to intersection node has a non-NULL value, reset it to None, and reset intersection bool to False
#     # if loop exits and intersection values are nullish, return None, else, return the intersection node
#     while current_A and current_B != None:
#         if (current_A == current_B) and (intersection_found == False):
#             intersection_found = True
#             intersection_node = current_A
#         elif (current_A != current_B) and (intersection_found == True):
#             intersection_found = False
#             intersection_node = None
#         current_A = current_A.next
#         current_B = current_B.next

#     return intersection_node