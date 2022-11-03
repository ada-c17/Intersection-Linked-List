


class Node:
    def __init__(self, value,):
        self.val = value
        self.next = None


    def intersection(headA, headB):
     
        current_headA  =  headA 
        while current_headA is not None:
            current_headB = headB
            while current_headB  is not None:
                if current_headA == current_headB:
                    return  current_headA
                else:
                    current_headB = current_headB.next
            current_headA = current_headA.next
        return None             


        """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """ 

    
       
    



   
  




  


     