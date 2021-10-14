class Node:

    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
def findPath( root, path, k):
 

    if root is None:
        return False
 

    path.append(root.key)
 

    if root.key == k :
        return True

    if ((root.left != None and findPath(root.left, path, k)) or (root.right!= None and findPath(root.right, path, k))):
        return True
 
    
    path.pop()
    return False
 
def leafnodearray(root,array):
	if root == None:
		return False
	
	if root.left == None and root.right==None:
		array.append(root.key)
		#print(root.key)
		return True
	
	leafnodearray(root.left,array)
	leafnodearray(root.right,array)
	
	
	
	return False
#########defining Tree############
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
##############EOD tree###############

#0=same node 1 = sibling 2 = cousin 3 = 2nd cousin
s=0
#leaf=[8,9,10,11,12,13,14,15]
leaf = []
leafnodearray(root,leaf)

s=0
for i in range(len(leaf)):
	for j in range(len(leaf)):
		path1 = []
		findPath(root,path1,leaf[i])
		path2 = []
		findPath(root,path2,leaf[j])
		n = len(path1)
		l=0
		for k in range(len(path1)):
			if path1[n-1-k] != path2[n-1-k]:
				l = l+2
		s = s+l

print(s)
e = s/(len(leaf)*len(leaf))
print(e)

