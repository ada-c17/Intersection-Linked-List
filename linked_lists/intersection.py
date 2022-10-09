


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

#  time complexity O(n)
#  space complexity O(n)
def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if headA is None or headB is None:
        return None
    elif headA is None and headB is None:
        return None
    else:
        current = headA
        nodes_set = set()
        while current:
            if current not in nodes_set:
                nodes_set.add(current)
            current = current.next
            
        current_b =  headB   
        while current_b:
            if current_b in  nodes_set:
                return current_b
            current_b = current_b.next   
        return None
        