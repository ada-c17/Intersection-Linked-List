


from queue import Empty


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    if headA is None or headB is None: # check to see if either heads are empty
        return None
    seen = []
    while headA:
        seen.append(headA) #append the first item
        headA = headA.next # assign the headA to next so the next item can get appended
    while headB: # iterate through the second LL
        if headB in seen: # check to see if the first item is in the seen list
            return headB # return if it is
        headB = headB.next # if not go to the next item in the LL
    return None # if nothing is found return None

        
        