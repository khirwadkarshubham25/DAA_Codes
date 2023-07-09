import time

from searching_algorithms.searching_algorithms_helper.searching_algorithms_service_helper import \
    SearchingAlgorithmsServiceHelper
from utils.tree_nodes import RedBlackTreeNullNode


class RedBlackTreeSearch(SearchingAlgorithmsServiceHelper):
    def get_data(self, data_list, item):
        """
        This function will start the execution of red black tree search algorithm. It will insert the data in tree and will
        create a BST and then search the item in tree.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of red black tree search function
        """
        r = None
        for key in data_list:
            r = self.insert_node(r, self.initialize_red_black_tree_node(key))  # # It will insert every number in red black tree.
        start_time = time.time()
        self.search_node(r, item)
        end_time = time.time()
        return start_time, end_time

    def insert_node(self, root, node):
        """
        This function will execute the insertion of red black tree search algorithm
        :param root: Root of BST
        :param node: Node to be inserted in tree
        :return: root of the tree.
        """
        if not root:
            root = node
            root.left, root.right = (RedBlackTreeNullNode(), RedBlackTreeNullNode())  # It will assign null pos to left and right of new pos.
            return root
        parent_node = self.get_parent_node(root, node)
        if parent_node is False:  # If number is already in tree. It will return the root.
            return root

        # Assign parent to pos. If pos value is less than, pos will be at left of parent, else the pos will be at
        # right of parent.
        node.parent = parent_node
        node.left, node.right = (RedBlackTreeNullNode(), RedBlackTreeNullNode())
        if not parent_node:
            root = node
        elif node.value < parent_node.value:
            parent_node.left = node
        elif node.value > parent_node.value:
            parent_node.right = node
        self.reconstruct_tree(root, node)

    @staticmethod
    def get_parent_node(root, node):
        """
        This function will find the parent for new pos.
        :param root: Root of the tree
        :param node: Node to be inserted
        :return: Parent Node of new pos
        """
        current_node, parent_node = (root, None)
        while not current_node:
            parent_node = current_node
            if node.value < parent_node.value:
                current_node = current_node.left
            elif node.value > parent_node.value:
                current_node = current_node.right
            else:
                return False
        return parent_node

    def reconstruct_tree(self, root, node):
        """
        This function will reconstruct the tree, so it will follow all the rules of red black tree.
        :param root: Root of the tree.
        :param node: New pos inserted
        :return: Root of the tree
        """
        while root != node and node.parent.color == 'red':  # When the new pos is not root and color of the parent of the pos is red.
            if node.parent == node.parent.parent.left:  # If pos parent is left pos of grandparent.
                uncle_node = node.parent.parent.right  # Uncle will be right pos of grandparent of new pos.
                if uncle_node.color == 'red':  # If the uncle is red
                    uncle_node.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:   # If uncle is black
                    if node == node.parent.right:   # if pos is to the right of its parent.
                        node = node.parent
                        root = self.left_rotation(root, node)  # Left rotate new nodes parent
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    root = self.right_rotation(root, node.parent.parent)  # Then do right rotation
            elif node.parent == node.parent.parent.right:   # If pos parent is to the right of grandparent of new pos.
                uncle_node = node.parent.parent.left    # Uncle will be left pos of grandparent of new pos
                if uncle_node.color == 'red':   # If uncle is red
                    uncle_node.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:    # If pos is left to its parent.
                        node = node.parent
                        root = self.right_rotation(root, node)  # Right rotate new nodes parent
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    root = self.left_rotation(root, node.parent.parent)    # Then do left rotation
        root.color = 'black'

    @staticmethod
    def left_rotation(root, node):
        """
        This function will do left rotation on pos.
        :param root: Root of the tree
        :param node: Node which has to be rotated.
        :return: root
        """
        temp_node = node.right
        node.right = temp_node.left
        if temp_node.left != RedBlackTreeNullNode():
            temp_node.left.parent = node

        temp_node.parent = node.parent
        if not node.parent:
            root = temp_node
        elif node == node.parent.left:
            node.parent.left = temp_node
        else:
            node.parent.right = temp_node
        temp_node.left = node
        node.parent = temp_node
        return root

    @staticmethod
    def right_rotation(root, node):
        """
        This function will do right rotation on pos.
        :param root: Root of the tree
        :param node: Node which has to be rotated.
        :return: root
        """
        temp_node = node.left
        node.left = temp_node.right
        if temp_node.right != RedBlackTreeNullNode():
            temp_node.right.parent = node

        temp_node.parent = node.parent
        if not node.parent:
            root = temp_node
        elif node == node.parent.right:
            node.parent.right = temp_node
        else:
            node.parent.left = temp_node
        temp_node.right = node
        node.parent = temp_node
        return root
