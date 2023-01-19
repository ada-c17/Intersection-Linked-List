


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
def find_intersection(headA, headB):
  len_lla = 0
  lla_current = headA
  while lla_current:
    len_lla += 1
    lla_current = lla_current.next
  
    len_llb = 0
    llb_current = headB
    while llb_current:
      len_llb += 1
      llb_current = llb_current.next

#traverse the list by prioritizing the longer of the two list options
  lla_current = headA
  llb_current = headB

  if len_lla > len_llb:
    for i in range(len_lla - len_llb):
      lla_current = lla_current.next
  else:
    for i in range(len_llb - len_lla):
      llb_current = llb_current.next

  while lla_current and llb_current:
    if lla_current == llb_current:
      return lla_current

    lla_current == lla_current.next
    llb_current == llb_current.next
    
  return None


