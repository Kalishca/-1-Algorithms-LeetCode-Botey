class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Поиск удаляемого узла и его родителя
        node = root
        parent = None
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
        if not node:
            return root

        # Случай 1: нет левого ребёнка – замена правым поддеревом
        if node.left is None:
            if parent is None:
                return node.right
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            return root

        # Случай 2: нет правого ребёнка – замена левым поддеревом
        if node.right is None:
            if parent is None:
                return node.left
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return root

        # Случай 3: есть оба ребёнка
        # Поиск преемника (минимального узла в правом поддереве) и его родителя
        succ = node.right
        succ_parent = node
        while succ.left:
            succ_parent = succ
            succ = succ.left

        # Если преемник не является прямым правым ребёнком
        if succ_parent != node:
            # Перемещаем правого ребёнка преемника на его место
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
            # Правое поддерево удаляемого узла становится правым поддеревом преемника
            succ.right = node.right

        # Замена удаляемого узла преемником
        if parent is None:
            root = succ
        elif parent.left == node:
            parent.left = succ
        else:
            parent.right = succ

        # Левое поддерево удаляемого узла становится левым поддеревом преемника
        succ.left = node.left

        return root