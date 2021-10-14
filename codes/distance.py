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

path1 = []
findPath( root, path1, 8)
#print(path1)

path2 = []
findPath( root, path2, 11)
#print(path2)

l=0
n = len(path1)
for i in range(n):
	if path1[n-i-1] != path2[n-1-i]:
		l = l+1
print("generation gap between",8,'',11,"is = ",l)
print("where 0=same node 1 = sibling 2 = cousin 3 = 2nd cousin and so on")
print("Path length between the 2 nodes = ",2*l)

