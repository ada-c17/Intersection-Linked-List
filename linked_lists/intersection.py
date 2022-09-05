


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    if headA is None or headB is None:
        return None
    node1 = headA
    node2 = headB
    while node1 != node2:
        node1 = node1.next if node1 else headB
        node2 = node2.next if node2 else headA
    return node1