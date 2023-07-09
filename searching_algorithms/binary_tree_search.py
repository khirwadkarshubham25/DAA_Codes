import time

from searching_algorithms.searching_algorithms_helper.searching_algorithms_service_helper import \
    SearchingAlgorithmsServiceHelper


class BinaryTreeSearch(SearchingAlgorithmsServiceHelper):
    def get_data(self, data_list, item):
        """
        This function will start the execution of binary tree search algorithm. It will insert the data in tree and will
        create a BST and then search the item in tree.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of binary tree search function
        """
        r = None
        for key in data_list:
            r = self.insert_node(r, self.initialize_binary_search_tree_node(key))  # It will insert every number in tree.
        start_time = time.time()
        self.search_node(r, item)
        end_time = time.time()
        return start_time, end_time

    def insert_node(self, root, node):
        """
        This function will execute the insertion binary tree search algorithm
        :param root: Root of BST
        :param node: Node to be inserted in tree
        :return: root of the tree.
        """
        if not root:
            root = node
        elif root.value < node.value:
            root.right = self.insert_node(root.right, node)
        else:
            root.left = self.insert_node(root.left, node)
        return root

