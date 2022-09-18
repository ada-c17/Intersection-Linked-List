
from os import curdir


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # method to add more nodes to linked list
#     def add_first(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
    

#     # method to return head of linked list
#     def getHead(self):
#         return self.head
    
#     def getNthNode(self, n):
#         current = self.head
#         while(current != None and n > 0):
#             current = current.next
#             n -=1;
        
#         return current

#adding nodes to both lists
node_d1 = Node("D")
node_e1 = Node("E")
node_f1 = Node("F")

node_c1 = Node("C")
node_e2 = Node("E")
node_f2 = Node("F")

#List A: [d, e1, f1]
node_d1.next = node_e1
node_e1.next = node_f1

#List B: [c, e2, f2]
node_c1.next = node_e2
node_e2.next = node_f2
node_f2.next = node_e1

head_a = node_d1
head_b = node_c1

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
    while long_list!=None and short_list!=None and long_list is not short_list:
        long_list=long_list.next
        short_list=short_list.next
        

    if  long_list!=None:
        return long_list
    else:
        return None 


def printLinkList(head):
    while head != None:
        print(head.val, end='->')
        head = head.next
    print()

print(intersection_node(head_a, head_b).val)
print("---------------")

print("---------------")
print("---------------")
