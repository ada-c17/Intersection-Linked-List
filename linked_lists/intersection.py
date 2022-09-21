
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


# first go around at brute force
def intersection_node_brute(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
        O(n*m) time complexity, where n and m are length of each list
        O(1) space complexity
    """    

    currentA = headA

    while currentA:
        currentB = headB
        while currentB:
            print(currentA, currentB)
            if currentB == currentA:
                return currentA
            currentB = currentB.next
        currentA = currentA.next


# hash map to speed things up. we'll call this my submitted solution
def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
        O(n+m) time complexity, where n and m are length of each list
        O(n) space complexity, where n is length of list of headA
    """    
    node_hash = {}
    currentA = headA
    currentB = headB

    while currentA:
        node_hash[currentA] = 1
        currentA = currentA.next
    
    while currentB:
        if currentB in node_hash:
            return currentB
        currentB = currentB.next


# This was the start of my third attempt at something neater. 
# I thought it through as: 
    # Traverse each list to find the length
    # Find the difference between the lengths
    # On the longer list, traverse forward that many from the head. 
    # From there, compare to the head of the shorter list to see 
        # if they are the same. 
    # Increment simultaneously until you find the node intersection.
def intersection_node_best(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
        O(n+m) time complexity, where n and m are length of each list
        O(1) space complexity, where n is length of list of headA
    """    

    # Bad news: it is an UGLY number of while loops to write.
    # The internet suggested the thinknig was right,
    # but the implementation could be better. But
    # tbh I never would have come up with it this way!
    # I miss arrays.

    currentA = headA
    currentB = headB

    while currentA != currentB:
        currentA = currentA.next if currentA else headB
        currentB = currentB.next if currentB else headA
    return currentA