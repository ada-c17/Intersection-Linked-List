


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.

        Full disclaimer: I've done this leetcode question before with my tutor and so I had this solution - that's the only reason it's so elengant, lol. I initially
        tried it with a hash set, but this solution has better space complexity
    """
    node_1, node_2 = headA, headB

    while node_1 != node_2:
        node_1 = node_1.next if node_1 else headB
        node_2 = node_2.next if node_2 else headA
    return node_2