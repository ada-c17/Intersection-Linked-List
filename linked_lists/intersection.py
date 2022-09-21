


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    # def search(self, value):
    #     current = self.head

    #     while current:
    #         if current.val == value:
    #             return True
    #         current = current.next
        
    #     return False


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    list_a = []
    list_b = []
    
    current = headA
    while current != None:
        list_a.append(current.val)
        current = current.next

    current = headB
    while current != None:
        list_b.append(current.val)
        current = current.next

    if not list_a or not list_b:
        return None

    # intersect_node_index = None
    # for i in range(len(list_a)):
    #     if list_a[i] == list_b[i]:
    #         intersect_node_index = i
    #         if list_a[i:] != list_b[i:]:
    #             return None

    # List A: ["D", "E", "F", "1", "2", "3"]
    # List B: ["X", "1", "2", "3"]
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)

    current = headA
    while current:
        for item in intersection:
            if current.val == item:
                return current
        current = current.next

    return None
