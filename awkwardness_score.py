class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.sums = 0
        self.flag = ''


def minAwkwardness(root): 
    # Base Case 
    if root is None: 
        return 0
    else:  
        if root.left is None and root.right is None: 
            if root.data < 0 :
                root.sums = root.data
            else: 
                #root.flag = 'N'
                root.sums = 0
            return root.sums
                     
        child=0
        grandchild=0
        LEFT =  minAwkwardness(root.left) 
        RIGHT = minAwkwardness(root.right)
        child = LEFT + RIGHT
        print('================================DATA: ',  root.data, '================================')
        if root.left :
            LEFT = root.left.data
            print('>>>>>>>  LEFT: ',  LEFT)
            
            if root.left.left:
                grandchild =  grandchild + root.left.left.sums
            if root.left.right:
                grandchild =  grandchild + root.left.right.sums            
            if root.left.left is None and root.left.right is None:
                grandchild =  0 #graindchild + root.left.sums
            
        if root.right :  
            RIGHT = root.right.data
            print('>>>>>>>  RIGHT: ',  RIGHT)
            if root.right.right:
                grandchild =  grandchild + root.right.right.sums
            if root.right.left:
                grandchild =  grandchild + root.right.left.sums                
            if root.right.left is None and root.right.right is None:
                grandchild = 0 # graindchild + root.right.sums

        print('>>>>>>>  graindchild: ',  grandchild)
        print('>>>>>>>  child + SELF: ',  child+ root.data)

        if child + root.data < 0:        
            if grandchild < child + root.data:
                root.sums = grandchild
                root.flag = 'N'            
            else:                    
                root.sums = child + root.data
        #minSum = root.sums

        print('>>>>>>>  root.sums: ',  root.sums)
        if root.left:
            print('>>>>>>>  Left.sums: ',  root.left.sums)
        if root.right:    
            print('>>>>>>>  Right.sums: ',  root.right.sums)
        return root.sums



### CASE -62
root = Node(0) 
root.left = Node(-20) 
root.right = Node(-1) 
root.right.left = Node(-1) 
root.right.right = Node(1) 

root.left.left = Node(20) 
root.left.right = Node(40) 

root.left.left.left = Node(-15) 
root.left.left.right = Node(0) 


root.left.right.left= Node(-45) 
root.left.right.right= Node(10) 

'''
### CASE -16
root = Node(0) 
root.right = Node(-1) 
root.right.left = Node(-1) 
root.right.right = Node(1) 

root.left = Node(-2) 
root.left.left = Node(2) 
root.left.right = Node(4) 

root.left.left.left = Node(-3) 
root.left.left.right = Node(0) 


root.left.right.left= Node(-5) 
root.left.right.left.left= Node(2) 
root.left.right.left.right= Node(3)

root.left.right.right= Node(1) 
root.left.right.right.left= Node(4) 
root.left.right.right.right= Node(0) 

root.left.right.right.right.left= Node(-2) 
root.left.right.right.right.right= Node(-4) 
'''


'''
###CASE -11
root = Node(0) 
root.right = Node(-1) 
root.right.left = Node(-1) 
root.right.right = Node(1) 

root.left = Node(-2) 
root.left.left = Node(2) 
root.left.right = Node(-1) 

root.left.left.left = Node(-3) 
root.left.left.right = Node(0) 


root.left.right.left= Node(-5) 

root.left.right.right= Node(20) 
root.left.right.right.left= Node(4) 
root.left.right.right.right= Node(-4) 
'''


print ("\n\nminimum awkwardness score: ", minAwkwardness(root) )