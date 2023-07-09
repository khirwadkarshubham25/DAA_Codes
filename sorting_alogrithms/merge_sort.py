import time


class MergeSort:

    def get_data(self, data_list, *args):
        """
        This function will start the execution of linear search algorithm.
        :param data_list: Input data list
        :param item: Item to search in list
        :return: Start time and end time of linear search function
        """
        start_time = time.time()
        item_loc = self.merge_sort(data_list)
        end_time = time.time()
        return start_time, end_time

    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            l = self.merge_sort(data[:mid])
            r = self.merge_sort(data[mid:])

            return self.merge(l, r)
        return data

    def merge(self, arr1, arr2):

        arr = []

        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                arr.append(arr1.pop(0))

            else:
                arr.append(arr2.pop(0))

        while arr1:
            arr.append(arr1.pop(0))

        while arr2:
            arr.append(arr2.pop(0))

        return arr


if __name__ == '__main__':
    print(MergeSort().merge_sort([3, 2, 5, 1, 7, 4, 9, 6]))
