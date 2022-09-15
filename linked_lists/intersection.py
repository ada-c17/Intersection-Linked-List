class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

   
def intersection_node(headA, headB):
    nodes = set()
    
    it = headA
    while not it is None:
        nodes.add(it)
        it = it.next
    
    it = headB
    while not it is None:
        if it in nodes:
            return it
        it = it.next
    
    return None


