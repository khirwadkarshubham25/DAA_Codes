import time


class BubbleSort:
    def __init__(self):
        pass

    def get_data(self, data_list, *args):
        """
        This function will start the execution of linear search algorithm.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of linear search function
        """
        start_time = time.time()
        item_loc = self.bubble_sort(data_list)
        end_time = time.time()
        return start_time, end_time

    @staticmethod
    def bubble_sort(data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j + 1] < data[j]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data


if __name__ == '__main__':
    BubbleSort().bubble_sort([2, 5,1, 7, 8,9])