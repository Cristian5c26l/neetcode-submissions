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
         
    def insertHelper(self, root, key, val):
        if not root:
            return TreeNode(key, val)

        if key > root.key:
            root.right = self.insertHelper(root.right, key, val)
        elif key < root.key:
            root.left = self.insertHelper(root.left, key, val)
        else:
            #root.key = key
            root.val = val

        return root

    def get(self, key: int) -> int:

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

    def removeHelper(self, root, key):

        if not root:
            return None
        
        if key > root.key:
            root.right = self.removeHelper(root.right, key)
        elif key < root.key:
            root.left = self.removeHelper(root.left, key)
        else:

            if not root.left:# 0 or 1 child
                return root.right
            elif not root.right:
                return root.left
            else:# 2 childs
                
                #right_child_min = root.right# Replace the properties key and value of root node to remove, by the minimum node of its right children
                #while right_child_min and right_child_min.left:
                #    right_child_min = right_child_min.left

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




