


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    list_a = []
    list_b = []
    # intersect_dict = {}
    
    current = headA
    while current.next != None:
        list_a.append(current.value)
        current = current.next

    current = headB
    while current.next != None:
        list_b.append(current.value)
        current = current.next

    if len(list_a) != len(list_b):
        return None

    # intersect_node_index = None
    for i in range(len(list_a)):
        if list_a[i] == list_b[i]:
            intersect_node_index = i
            if list_a[i:] != list_b[i:]:
                return None
    
    intersect_node = headA
    for j in range(1, intersect_node_index):
        intersect_node = intersect_node.next
    return intersect_node



    # for i in range(len(list_a)):
    #     intersect_dict[i] = True if list_a[i] == list_b[i] else False

    # # {0: false, 1: false, 2: true, 3: true, 4:true}
    # # OR
    # # {0: false, 1: false, 2: true, 3: false, 4:true}

    # for index, value in intersect_dict.items():
    #     if value:
            


    # intersect_node_index = None
    # currentA = headA
    # currentB = headB

    # while currentA and currentB:
    #     if currentA.value == currentB.value:
    #         intersect_node_a = currentA
    #         intersect_node_b = currentB
    #         while intersect_node_a.next and intersect_node_b.next and intersect_node_a.next.value == intersect_node_b.next.value:
                
    #     currentA = currentA.next
    #     currentB = currentB.next
