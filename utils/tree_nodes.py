class BinarySearchTreeNode:
    """
    Binary Search Tree Node
    """
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


class RedBlackTreeNode:
    """
    Red Black Tree Node
    """
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.color = 'red'
        self.parent = None


class RedBlackTreeNullNode:
    """
    Red Black Tree Null Node.
    """
    def __init__(self):
        self.left = None
        self.right = None
        self.value = -1
        self.color = 'black'
