


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):

    current_a = headA
    current_b = headB
    hash_map = {}

    if not current_a or not current_b:
        return None

    while current_a:
        hash_map[current_a] = 1
        current_a = current_a.next

    while current_b:
        if current_b in hash_map.keys():
            return current_b
        current_b = current_b.next
    
    return None

    



