


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.

        - set var to track whether lists intersect equal to false
        - set both current nodes equal to head nodes
        - matching nodes = []
    
        - while current node exists for both lists:
        - if both current nodes are equal to each other, append current node value to matching nodes array
        - and set do_intersect equal to true
        - set both current nodes to next nodes

        - if do_intersect: return matching_nodes[0] else return None
    """
    # do_intersect = False
    # current_node_a = headA
    # current_node_b = headB

    # matching_values = []

    # while current_node_a.val and current_node_b.val:
    #     if current_node_a.val == current_node_b.val:
    #         matching_values.append(current_node_a.val)
    #         do_intersect = True
    #     else:
    #         do_intersect = False
        
    #     current_node_a = current_node_a.next
    #     current_node_b = current_node_b.next
    
    # return matching_values[0] if do_intersect else None

    do_intersect = False
    current_node_a = headA.next
    current_node_b = headB.next

    matching_values = []

    while current_node_a.val and current_node_b.val:
        if current_node_a.val == current_node_b.val:
            matching_values.append(current_node_a.val)
            do_intersect = True
        else:
            do_intersect = False
        
        current_node_a = current_node_a.next
        current_node_b = current_node_b.next
    
    return Node(matching_values[0]) if do_intersect else None