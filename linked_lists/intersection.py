


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

    list_of_nodes = []
    current = headB
    while current != None:
      list_of_nodes.append(current)
      current = current.next
    
    currentA = headA
    while currentA != None:
      if currentA in list_of_nodes:
        return currentA
      else:
        currentA = currentA.next
    #loop through listA unknown nodes to see if present in listB. 
    return None