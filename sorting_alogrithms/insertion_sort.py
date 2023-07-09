import time


class InsertionSort:

    def get_data(self, data_list, *args):
        """
        This function will start the execution of linear search algorithm.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of linear search function
        """
        start_time = time.time()
        item_loc = self.insertion_sort(data_list)
        end_time = time.time()
        return start_time, end_time

    @staticmethod
    def insertion_sort(data):

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j > -1 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

        return data


if __name__ == '__main__':
    InsertionSort().insertion_sort([2, 5, 1, 8, 3, 4, 9, 6])