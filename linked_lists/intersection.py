class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def add_nodes_to_list(head):
        current = head
        node_list = []
        while current is not None:
            node_list.append(current)
            current = current.next
        return node_list


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    # If either is an empty list, return none:
    if not headA or not headB:
        return None
    # Add all nodes (not just values) to lists, for easier comparing:
    listA = Node.add_nodes_to_list(headA)
    listB = Node.add_nodes_to_list(headB)
    # nested loops: iterate thru list A, look for equality with B
    # then compare subsequent items in list
    for index_a in range(len(listA)):
        for index_b in range(len(listB)):
            if listA[index_a] == listB[index_b]:
                # check whether remaining list lengths are equal
                if len(listB)-index_b != len(listA)-index_a:
                    return None
                for i in range(len(listA)-index_a-1):
                    i += 1
                    if listA[index_a+i] == listB[index_b+i]:
                        print(listA[index_a+i])
                    else:
                        return None
                return listA[index_a]
    return None
