


class Node:
    def __init__(self, value, next=None, previous=None):
        self.val = value
        self.next = next
        self.previous = next

def transform_to_doubly_linked_list(head):
    previous = None
    current = head
    print(head)
    while current is not None:
        current.previous = previous
        previous = current
        current = current.next

    return previous


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """

    if not headA or not headB:
        return None
    currentA = headA
    currentB = headB

    while currentA is not currentB:
        if currentA == None:
            currentA = headB
            continue
        if currentB == None:
            currentB = headA
            continue
        currentA = currentA.next
        currentB = currentB.next

    return currentA
        
    

    

    
    
    
    
    