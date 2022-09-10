


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def reverse_node_list(head):
    node_list = []
    current = head
    while current:
        node_list.append(current)
        current = current.next
    node_list.reverse()
    return node_list

def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None
    
    listA, listB = reverse_node_list(headA), reverse_node_list(headB)
    i, limit = 0, min(len(listA), len(listB))
    result = None

    while i < limit and listA[i] == listB[i]:
        result = listA[i]
        i += 1
    return result