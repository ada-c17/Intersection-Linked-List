


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    # def search(self, value):
    #     current = self.head

    #     while current:
    #         if current.val == value:
    #             return True
    #         current = current.next
        
    #     return False


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    list_a = []
    list_b = []
    
    current = headA
    while current != None:
        list_a.append(current.val)
        current = current.next

    current = headB
    while current != None:
        list_b.append(current.val)
        current = current.next

    if not list_a or not list_b:
        return None

    # intersect_node_index = None
    # for i in range(len(list_a)):
    #     if list_a[i] == list_b[i]:
    #         intersect_node_index = i
    #         if list_a[i:] != list_b[i:]:
    #             return None

    # List A: ["D", "E", "F", "1", "2", "3"]
    # List B: ["X", "1", "2", "3"]


    # need to find the intersection without using a list as I need 
    # the intersection values to be in order I think
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)

    if not intersection:
        return None

    # current = headA
    # while current:
    #     for item in intersection:
    #         if current.val == item:
    #             return current
    #     current = current.next

    currentA = headA
    currentB = headB
    intersect = None

    while currentA and currentB:
        for item in intersection:
            if currentA.val == item and currentB.val == item:
                if currentA == currentB:
                    if intersect == None:
                        intersect = currentA
                    currentA = currentA.next
                    currentB = currentB.next
                    break
            elif currentB.val == item:
                currentA = currentA.next
                break
            elif currentA.val == item:
                currentB = currentB.next
                break
            else:
                currentA = currentA.next
                currentB = currentB.next
                break
    return intersect 

    return None
