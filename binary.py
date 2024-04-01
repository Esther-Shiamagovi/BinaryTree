class Node:
    def __init__ (self,key):
        self.left = None
        self.right = None
        self.val = key
        
        def insert(root,key):
            if root is None:
                return Node(key)
            else:
        
                if root.val==key:
                    return root
                elif root.val < key:
                    root.right=insert(root.right,key)
                else:
                    root.left = insert(root.left,key)
                return root
                
                def inorder(root):
                    if root:
                        inorder(root.left)
                        print(root.val,end=" ")
                        inorder(root.right)
                        
                        if __name__=='_main_':
                            
                            t=Node(20)
                            t=insert(t,21)
                            t=insert(t,15)
                            t=insert(t,10)
                            t=insert(t,9)
                            t=insert(t,32)
                            t=insert(t,25)
                    
                    inorder(t)
                
                
                
  
            
    