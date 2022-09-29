


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):

    currentA = headA
    currentB = headB

    if not currentA or not currentB:
        return None

#Nodes will be same place in memory so we don't need to check values.
    while currentA != currentB:
        if currentA == None:
            currentA = headB
        else:
            currentA = currentA.next

        if currentB == None:
            currentB = headA
        else:
            currentB = currentB.next

    return currentA




# Different Length Lists

# linked_list_a: 3 -> 4 -> 5 -> 6 -> 7
# linked_list_b: 4 -> 5 -> 6 -> 7

# After traversing each list set list a to list b and list b to list a so that they are able to sync up.
# 3 -> 4 -> 5 -> 6 -> 7 -> 4 -> 5 -> 6 -> 7
# 4 -> 5 -> 6 -> 7 -> 3 -> 4 -> 5 -> 6 -> 7
