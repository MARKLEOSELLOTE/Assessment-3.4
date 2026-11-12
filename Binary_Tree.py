from collections import deque

LABELS = {1: "S", 2: "E", 3: "L", 4: "L", 5: "O", 6: "T", 7: "E"}


def show(order):
    return " - ".join(LABELS[n] for n in order)


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_tree():
    n = {k: TreeNode(k) for k in LABELS}
    n[1].left, n[1].right = n[2], n[3]
    n[2].left, n[2].right = n[4], n[5]
    n[3].left, n[3].right = n[6], n[7]
    return n[1]


def tree_bfs(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.key)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def tree_dfs(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.key)
    tree_dfs(node.left, result)
    tree_dfs(node.right, result)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("BFS:", show(tree_bfs(root)))
    input("Enter to see DFS")
    print("DFS:", show(tree_dfs(root)))