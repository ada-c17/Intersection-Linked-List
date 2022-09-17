


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if not headA or not headB:
        return None
    
    currentA = headA
    currentB = headB

    while currentA.next and currentB.next:
        print(currentA.val, currentB.val)
        if currentA == currentB:
            return currentA
        currentA = currentA.next
        currentB = currentB.next
        # print(currentA.val, currentB.val)
    return None
        

# node_d = Node("D")
# node_e = Node("E")
# node_f = Node("F")

# node_x = Node("X")
# node_y = Node("Y")
# node_z = Node("Z")

# node_one = Node("1")
# node_two = Node("2")
# node_three = Node("3")
# node_one.next = node_two
# node_two.next = node_three

# # List A: ["D", "E", "F", "1", "2", "3"]
# node_d.next = node_e
# node_e.next = node_f
# node_f.next = node_one

# # List B: ["X", "Y", "Z", "1", "2", "3"]
# node_x.next = node_y
# node_y.next = node_z
# node_z.next = node_one

# head_a = node_d
# head_b = node_x

# # Act
# print(intersection_node(head_a, head_b))