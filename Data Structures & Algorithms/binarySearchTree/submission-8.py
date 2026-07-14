class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        root = self.root
        self.root = self.insertHelper(root, key, val)

        #print("VER ", self.root.key)
        #curr = self.root
        #self.showInOrderTraversal(curr)
         
    def insertHelper(self, root, key, val):# O(logn), where n is the total nodes of the tree
        if not root:
            return TreeNode(key, val)

        if key > root.key:
            root.right = self.insertHelper(root.right, key, val)# Build right children
        elif key < root.key:
            root.left = self.insertHelper(root.left, key, val)# Build left children
        else:
            #root.key = key
            root.val = val

        return root

    def get(self, key: int) -> int:# O(logn)

        if not self.root:
            return -1

        root = self.root
        while root:
            if key > root.key:
                root = root.right
            elif key < root.key:
                root = root.left
            else:
                return root.val 

        return -1


    def getMin(self) -> int:

        if not self.root:
            return -1

        root = self.root
        while root and root.left:
            root = root.left
        
        return root.val



    def getMax(self) -> int:

        if not self.root:
            return -1

        root = self.root
        while root and root.right:
            root = root.right
        
        return root.val

    def remove(self, key: int) -> None:
        curr = self.root
        self.root = self.removeHelper(curr, key)

    def removeHelper(self, root, key):#O(logn)

        if not root:
            return None
        
        if key > root.key:
            root.right = self.removeHelper(root.right, key)# Build right children
        elif key < root.key:
            root.left = self.removeHelper(root.left, key)# Build left children
        else:

            if not root.left:# 0 or 1 child
                return root.right
            elif not root.right:
                return root.left
            else:# 2 childs
 
                min_node = self.minNodeHelper(root.right)
                
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.removeHelper(root.right, root.key)

        return root


    def getInorderKeys(self) -> List[int]:
        ordered_keys = []
        curr = self.root
        self.getInOrderTraversal(curr, ordered_keys)
        return ordered_keys

    def getInOrderTraversal(self, curr, or_k):

        if not curr:
            return

        self.getInOrderTraversal(curr.left, or_k)
        or_k.append(curr.key)
        self.getInOrderTraversal(curr.right, or_k)

    def showInOrderTraversal(self, curr):

        if not curr:
            return

        self.showInOrderTraversal(curr.left)
        print(f"{curr.key} - {curr.val}")
        self.showInOrderTraversal(curr.right)

    def minNodeHelper(self, root):
        while root and root.left:
            root = root.left

        return root




