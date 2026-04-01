class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def preorder(node):
            if node is None:
                return
            result.append(node.val)   # обработать узел
            preorder(node.left)       # обойти левое поддерево
            preorder(node.right)      # обойти правое поддерево
        
        preorder(root)
        return result
        