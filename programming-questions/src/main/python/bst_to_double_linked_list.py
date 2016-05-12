'''
Convert a binary search tree to a sorted double-linked list. 
We can only change the target of pointers, but cannot create any new nodes.

'''




import sys



class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value
        self.prev = None
        self.next = None
    

def print_bst(root):
    return "(%s %s %s)" % (print_bst(root.left) if (root.left is not None) else "", root.value, print_bst(root.right) if (root.left is not None) else "")
    
    
def print_linked_list(head):
    
    ret = []
    while head is not None:
        ret.append(head.value)
        head = head.next
        
    return ret
    
    

def to_double_linked_list(root):
    (left_head, left_tail) = to_double_linked_list(root.left) if root.left is not None else (None, None)
    (right_head, right_tail) = to_double_linked_list(root.right) if root.right is not None else (None, None)
    
    #Rewire
    root.prev = left_tail
    root.next = right_head
    
    if left_tail is not None: left_tail.next = root 
    if right_head is not None: right_head.prev = root
    
    return (left_head if left_head is not None else root, right_tail if right_tail is not None else root)
    
    

if __name__ == '__main__':
    
    nleft = Node(None, None, -5)
    nright = Node(None, None, 6)
    root = Node(nleft, nright, 0)
    
    print print_bst(root)
    
    (head, tail) = to_double_linked_list(root)
    
    print print_linked_list(head)
    
    
    
    