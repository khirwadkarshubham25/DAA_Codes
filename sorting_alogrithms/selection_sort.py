import time


class SelectionSort:

    def get_data(self, data_list, *args):
        """
        This function will start the execution of linear search algorithm.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of linear search function
        """
        start_time = time.time()
        item_loc = self.selection_sort(data_list)
        end_time = time.time()
        return start_time, end_time

    @staticmethod
    def selection_sort(data):

        for i in range(len(data)):
            min_idx = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j

            data[i], data[min_idx] = data[min_idx], data[i]

        return data


if __name__ == '__main__':
    SelectionSort().selection_sort([2, 4, 1, 6, 3, 8, 5, 9])
