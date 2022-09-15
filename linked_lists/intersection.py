


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    list_a = headA
    list_b = headB
    array_a = []
    array_b = []

    # make a list for each
    while list_a or list_b:
        if list_a:
            array_a.append(list_a)
            list_a = list_a.next
        if list_b:
            array_b.append(list_b)
            list_b = list_b.next

    # compare lists backwards
    count = 0
    if (len(array_a) > 0) and (len(array_b) > 0):
        for i in range(-1, -(len(array_a)), -1):
            if array_a[i] != array_b[i]:
                break
            count += 1
    
    result = None
    if count > 0:
        result = headA
        for i in range(len(array_a)-count):
            result = result.next
    
    return result