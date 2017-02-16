#The height of a binary tree is the number of edges between the tree's
#root and its furthest leaf. This means that
#a tree containing a single node has a height of .

#Complete the getHeight function provided in your editor so that
#it returns the height of a binary tree. This function has a parameter, ,
#which is a pointer to the root node of a binary tree.



def height(root):
    if root:
        lefth = height(root.left)
        righth = height(root.right)
        if lefth > righth:
            return lefth + 1
        else:
            return righth + 1
    else:
        return -1
