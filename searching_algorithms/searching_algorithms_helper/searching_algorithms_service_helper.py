import random
from abc import abstractmethod

from utils.tree_nodes import BinarySearchTreeNode, RedBlackTreeNode


class SearchingAlgorithmsServiceHelper:

    def search_node(self, root, val):
        """
        This function will search pos in binary search tree or red black tree
        :param root: Root of the tree
        :param val: Value to be seacrhed
        :return: True if value is found else False.
        """
        if not root:
            return False
        elif root.value == val:
            return True
        elif root.value < val:
            return self.search_node(root.right, val)
        elif root.value > val:
            return self.search_node(root.left, val)

    @staticmethod
    def initialize_binary_search_tree_node(val=None):
        return BinarySearchTreeNode(value=val)

    @staticmethod
    def initialize_red_black_tree_node(val=None):
        return RedBlackTreeNode(value=val)

    @abstractmethod
    def get_data(self, data_list, item):
        pass
