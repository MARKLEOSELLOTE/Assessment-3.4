class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node, result):
    if node is None:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)


def build_tree():
    root = Node("K")

    root.left = Node("A")
    root.left.left = Node("M")
    root.left.right = Node("R")

    root.right = Node("E")
    root.right.left = Node("L")
    root.right.right = Node("O")

    return root


def main():
    root = build_tree()

    pre, ino, post = [], [], []
    preorder(root, pre)
    inorder(root, ino)
    postorder(root, post)

    print("MARK LEO")

    input("Press Enter to continue...")

    print()
    print("DFS Methods in Tree")
    print("-" * 70)
    print("\n1. PreOrder  (Root -> Left -> Right):")
    print("   " + " -> ".join(pre))
    print("\n2. InOrder   (Left -> Root -> Right):")
    print("   " + " -> ".join(ino))
    print("\n3. PostOrder (Left -> Right -> Root):")
    print("   " + " -> ".join(post))
    print("-" * 70)


if __name__ == "__main__":
    main()