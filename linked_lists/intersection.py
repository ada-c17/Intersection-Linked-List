import copy


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

    listA = []
    listB = []
    currentA = headA
    currentB = headB

    while currentA:
        while currentB.next:
            if currentB.val == currentA.val:
                inter = currentB
                match = check_match(currentA, currentB)
                if match:  
                    return inter
                else: 
                    return None
            else:
                currentB = currentB.next
        currentA = currentA.next
        currentB = headB
    return None

def check_match(currentA, currentB):
    while currentA and currentB:
        if currentA.val == currentB.val and currentA.next == currentB.next:
            currentA = currentA.next
            currentB = currentB.next
            match= True
        else:
            match = False
            break
    return match
    
    
           
# Arrange
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

node_x = Node("X")

node_one = Node("1")
node_two = Node("2")
node_three = Node("3")
node_one.next = node_two
node_two.next = node_three

# List A: ["D", "E", "F", "1", "2", "3"]
node_d.next = node_e
node_e.next = node_f
node_f.next = node_one

# List B: ["X", "1", "2", "3"]
node_x.next = node_one

head_a = node_d
head_b = node_x

# Act
answer = intersection_node(head_a, head_b)
print(f'Answer: {answer}')  