


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

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

    intersection_list = []

    while list_a[i] == list_b[i] and abs(i)<len(list_a):
        intersection_list.append(list_a[i])
        i -= 1

    if intersection_list:
        intersection_list.reverse()
    else:
        return None

    currentA = headA
    currentB = headB
    intersect = None

    while currentA and currentB:
        for item in intersection_list:
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