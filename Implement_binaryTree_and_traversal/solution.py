# first create a treeclass which represents each node in the binary tree
class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left= None
        self.right= None

# we can do it manually but As tree height increases it can be tough to do. 
# instead we can create a function that accepts an tuple and implement teh binary tree

# 2 is the rootnode since it is in teh center.
# ((1,3,None), 2,((None,3,4),5,(6,7,8)))

def parse_tuple (data):
    if isinstance(data,tuple)and len(data)== 3:
        node= TreeNode(data[1]) #middle element is the current node
        node.left = parse_tuple(data[0])  # used recursion to go in depth
        node.right= parse_tuple(data[2])
    elif data == None:
        node = None
    else:
        node=TreeNode(data)
    return node

tree2 = parse_tuple(((1,3,None), 2,((None,3,4),5,(6,7,8))))
print(tree2.key)
print(tree2.left.key, tree2.left.right)
print(tree2.right.left.right.key)



#*********** IN-ORDER TRAVERSAL ******************************

def inorder_traversal(node):
    if node is None:
        return []
    return(inorder_traversal(node.left)+ [node.key] + inorder_traversal(node.right)) 


# tree2 = parse_tuple(((1,3,None), 2,((None,3,4),5,(6,7,8))))

print (inorder_traversal(tree2))



#*********** Pre-ORDER TRAVERSAL ******************************

def preorder_traversal(node):
    if node is None:
        return []
    return ([node.key]+ preorder_traversal(node.left) + preorder_traversal(node.right))

print(preorder_traversal(tree2))

#*********** POST-ORDER TRAVERSAL ******************************

def postorder_traversal(node):
    if node is None:
        return []
    return ([node.key]+ postorder_traversal(node.right) + postorder_traversal(node.left))

print(postorder_traversal(tree2))