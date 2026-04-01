class Solution:
    def isValidBST(self, root):
        # Список для хранения значений узлов в порядке inorder-обхода
        result = []

        # Рекурсивная функция симметричного обхода (inorder tree walk)
        def inorder(node):
            if not node:
                return
            # Сначала обходим левое поддерево
            inorder(node.left)
            # Затем добавляем значение текущего узла
            result.append(node.val)
            # Затем обходим правое поддерево
            inorder(node.right)

        # Запускаем обход с корня
        inorder(root)

        # После обхода проверяем, что полученная последовательность строго возрастает
        for i in range(1, len(result)):
            # Если предыдущее значение больше или равно текущему — дерево не BST
            if result[i] <= result[i-1]:
                return False
        return True