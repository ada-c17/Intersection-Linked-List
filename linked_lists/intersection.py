
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # method to add more nodes to linked list
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to return head of linked list
    def getHead(self):
        return self.head

#adding nodes to both lists
ll1 = LinkedList()
ll1.add_first(6)
ll1.add_first(3)
ll1.add_first(2)
ll1.add_first(1)

headA = ll1.getHead()

ll2 = LinkedList()
ll2.add_first(6)
ll2.add_first(5)
ll2.add_first(4)

headB = ll2.getHead()

#get lenth of linked list
def get_lin_list_len(head):
    list_len=0
    current=head

    while current !=None:
        list_len+=1
        current=current.next
    return list_len


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return None.
    """
    #storing lenth of both linked lists
    len_headA=get_lin_list_len(headA)
    len_headB=get_lin_list_len(headB)

    short_list=None
    long_list=None

    difference=0
    
    # finding which list is longer and calculating the difference 
    if len_headA>len_headB:
        long_list=headA
        short_list=headB
        difference=len_headA-len_headB
    else:
        long_list=headB
        short_list=headA
        difference=len_headB-len_headA    
    
    # moving the pointer to next node to be on the same level both linked lists
    while difference>0:
        long_list=long_list.next
        difference-=1
    
    # looping over lists until they have the same value and returning the value if they intersect
    while long_list!=None and short_list!=None and long_list.val!=short_list.val:
        long_list=long_list.next
        short_list=short_list.next

    if  long_list!=None:
        return long_list.val
    else:
        return None 
 

def printLinkList(head):
    while head != None:
        print(head.val, end='->')
        head = head.next
    print()

print(intersection_node(headA, headB))
print("---------------")
printLinkList (headA)
printLinkList(headB)
print("---------------")
