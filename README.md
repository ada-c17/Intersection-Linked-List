# Intersection of Linked Lists

## Exercise
Given the heads of two singly linked-lists `head_a` and `head_b`, return the node at which the two lists intersect. If the two linked lists do not intersect, the function should return `None`.

For example, the following two linked lists begin to intersect at 5.

`linked_list_a: 3 -> 4 -> 5 -> 6 -> 7`

`linked_list_b: 1 -> 2 -> 5 -> 6 -> 7` 


There are no cycles anywhere in the linked list structures.

Assume any intersection includes the tails of each list. For example, the following scenario would not occur because while the node with value 5 is in the same place, the subsequent nodes are different.

`linked_list_a: 3 -> 4 -> 5 -> 6 -> 7`

`linked_list_b: 1 -> 2 -> 5 -> 4 -> 3` 

There are no cycles anywhere in the linked list structures. Assume any intersection includes the tails of each list.


The linked lists must retain their original structure after the function returns. 

## Getting Started

As usual with a python project, create a virtual environment:

```
python3 -m venv venv
```

Then activate the virtual environment

```
source venv/bin/activate
```

Then install the required packages.

```
pip install -r requirements.txt
```
