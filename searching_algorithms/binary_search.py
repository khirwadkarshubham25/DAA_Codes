import time

from searching_algorithms.searching_algorithms_helper.searching_algorithms_service_helper import \
    SearchingAlgorithmsServiceHelper


class BinarySearch(SearchingAlgorithmsServiceHelper):
    def get_data(self, data_list, item):
        """
        This function will start the execution of binary search algorithm.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of binary search function
        """
        data_list.sort()
        start_time = time.time()
        item_loc = self.binary_search(data_list, item)
        end_time = time.time()
        return start_time, end_time

    @staticmethod
    def binary_search(items, number):
        """
        This function will execute binary search algorithm
        :param items: List of input data
        :param number: Item to search in list
        :return: Item location
        """
        low = 0
        high = len(items) - 1
        while low <= high:
            mid = int((high + low) / 2)  # middle number of list.
            if number == items[mid]:  # If mid number is equal to item it will return the location of mid number
                return mid
            elif items[mid] < number:  # if the number is more than mid number, then it will choose the upper half of the list
                low = mid + 1
            elif items[mid] > number:  # if the number is less than mid number, then it will choose the lower half of the list
                high = mid - 1
        return
