
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def get_length(current):
    """
    Helper function to return length of linked lists.
    """
    length = 0
    while current:
        length += 1
        current = current.next
    return length

def intersection_node(headA, headB):
    """ 
    Will return the node at which the two lists intersect.
    If the two linked lists have no intersection at all, return None.
    """
    # Get length of both lists
    lenA, lenB = get_length(headA), get_length(headB)
    
    # Set pointer variables to head
    currentA, currentB = headA, headB

    # Because the linked lists intersect, we assume that if the lists are of different lengths, we can iterate through the difference, which accounts for the "extra" nodes in the beginning. This makes it so that we can compare the rest of the nodes in the two lists without worrying about the lengths.
    if lenA > lenB:
        for i in range(abs(lenA-lenB)):
            currentA = currentA.next
    else:
        for i in range(abs(lenA-lenB)):
            currentB = currentB.next

    # Now we can compare the two linked lists and check for matching nodes. 
    while currentA and currentB:
        if currentA == currentB:
            return currentA
        currentA = currentA.next
        currentB = currentB.next
    return None
