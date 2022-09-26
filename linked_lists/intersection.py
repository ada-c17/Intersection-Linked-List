


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    if headB == None or headA == None:
      return None

    #Append current node to new list
    list_of_nodes = []
    current = headB
    while current != None:
      list_of_nodes.append(current)
      current = current.next
    
    #Compare nodes from other list to new list to check intersection.
    currentA = headA
    while currentA != None:
      if currentA in list_of_nodes:
        return currentA
      else:
        currentA = currentA.next
    return None