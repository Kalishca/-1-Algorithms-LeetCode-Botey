class Solution:
    def postorderTraversal(self, root):
        result = []
        
        def postorder(node):
            if node is None:
                return
            postorder(node.left)   # обойти левое поддерево
            postorder(node.right)  # обойти правое поддерево
            result.append(node.val) # обработать узел
        
        postorder(root)
        return result