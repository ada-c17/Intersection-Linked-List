


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
    print(f"lista: {list_a}")

    current = headB
    while current != None:
        list_b.append(current.val)
        current = current.next
    print(f"listb: {list_b}")


    if not list_a or not list_b:
        return None

    # List A: ["D", "E", "F", "1", "2", "3"]
    # List B: ["X", "1", "2", "3"]

    # intersect_value = None

    intersection_list = []


    # a = 0
    # b = 0

    # while list_a[a] and list_b[b]:
    #     if
    
    # while list_a[a] and list_b[b]:
    #     if list_a[a] == list_b[b]:
    #         intersection_list.append(list_a[a])
    #         a += 1
    #         b += 1
    #     elif list_a[a] ==
    i=-1
    while list_a[i] == list_b[i] and abs(i)<len(list_a):
        intersection_list.append(list_a[i])
        i -= 1

    if intersection_list:
        intersection_list.reverse()
        print(f"intersection_list: {intersection_list}")
    else:
        return None
    


    # need to find the intersection without using a list as I need 
    # the intersection values to be in order I think
    # set_a = set(list_a)
    # set_b = set(list_b)
    # intersection = set_a.intersection(set_b)

    # if not intersection_list:
    #     return None

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

    return None
