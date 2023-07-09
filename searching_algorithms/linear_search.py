import time

from searching_algorithms.searching_algorithms_helper.searching_algorithms_service_helper import \
    SearchingAlgorithmsServiceHelper


class LinearSearch(SearchingAlgorithmsServiceHelper):

    def get_data(self, data_list, item):
        """
        This function will start the execution of linear search algorithm.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of linear search function
        """
        start_time = time.time()
        item_loc = self.linear_search(data_list, item)
        end_time = time.time()
        return start_time, end_time

    @staticmethod
    def linear_search(items, number):
        """
        This function will execute linear search algorithm
        :param items: List of input data
        :param number: Item to search in list
        :return: Item location
        """
        for i in range(len(items)):  # Traverse the input list
            if items[i] == number:  # If number found return its location
                return i
        return  
