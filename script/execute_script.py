import os
import random
import sys

import matplotlib.pyplot as plot_graph

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from searching_algorithms.binary_search import BinarySearch
from searching_algorithms.binary_tree_search import BinaryTreeSearch
from searching_algorithms.linear_search import LinearSearch
from searching_algorithms.red_black_tree_search import RedBlackTreeSearch
from sorting_alogrithms.bubble_sort import BubbleSort
from sorting_alogrithms.insertion_sort import InsertionSort
from sorting_alogrithms.merge_sort import MergeSort
from sorting_alogrithms.selection_sort import SelectionSort


class ExecuteScript:
    def __init__(self):
        self.algo_map = {
            1: 'Linear Search',
            2: 'Binary Search',
            3: 'Binary Search Tree',
            4: 'Red Black Tree',
            5: 'Bubble Sort',
            6: 'Insertion Sort',
            7: 'Merge Sort',
            8: 'Selection Sort'
        }
        self.algo_obj_map = {
            'Linear Search': LinearSearch(),
            'Binary Search': BinarySearch(),
            'Binary Search Tree': BinaryTreeSearch(),
            'Red Black Tree': RedBlackTreeSearch(),
            'Bubble Sort': BubbleSort(),
            'Insertion Sort': InsertionSort(),
            'Merge Sort': MergeSort(),
            'Selection Sort': SelectionSort()
        }

    def run_script(self):
        """
        This function will start the execution of script. It will choose the test type(single algorithm or
        multiple algorithm) and execute that test accordingly
        :return:
        """
        algo_x_y_values, graph_details = (None, None)
        # Choose test type.
        test_choice = self.choose_test_type()
        if test_choice == 1:
            # Single Algorithm test call
            algo_x_y_values, graph_details = self.run_single_algorithm_test()

        elif test_choice == 2:
            # Multiple Algorithm test call
            algo_x_y_values, graph_details = self.run_multiple_algorithm_test()
        self.create_graph(algo_x_y_values, graph_details)

    def run_single_algorithm_test(self):
        """
        This function will execute single algorithm test. It will generate the random data sets and will execute chosen
        algorithm on that data sets and will design a bar graph of result.
        :return: data_size_time_map: This will return the size of data and time needed for that algorithm to execute on
        that data size.
        :return: graph_details: This will return the graph details for single algorithm test results.
        """
        algo_choice = self.choose_algorithms(no_of_algo=1)
        data_count = random.randint(2, 5)
        data_size_time_map = {}
        for i in range(data_count):
            print('Generating Random input data.....')
            data_list, item = self.generate_random_input()
            print(f"Input: {data_list}")
            print(f'Item to search: {item}')
            start_time, end_time = self.algo_obj_map[self.algo_map[algo_choice]].get_data(data_list, item)
            data_size_time_map[len(data_list)] = (end_time - start_time) * 1000
        graph_details = {
            'name': f'{self.algo_map[algo_choice]} Graph with different data set.',
            'x_label': 'Data Size',
            'y_label': 'Time in milliseconds',
            'graph_type': 'bar'
        }
        return data_size_time_map, graph_details

    def run_multiple_algorithm_test(self):
        """
        This function will execute multiple algorithm test. It will give choice for input type data sets and will
        execute chosen algorithm on that data sets and will design a bar graph of result.
        :return: algorithm_time_dict: This will return the algorithm and its time to execute on that data size.
        :return: graph_details: This will return the graph details for single algorithm test results.
        """
        data_list, item = (None, None)
        input_choice = self.choose_input_type()
        if input_choice == 1:
            print('Generating Random input data.....')
            data_list, item = self.generate_random_input()
        elif input_choice == 2:
            data_list, item = self.get_user_input()
        else:
            print('Invalid input choice...')
        print(f"Input: {data_list}")
        print(f'Item to search: {item}')
        algo_list = self.choose_algorithms()
        algorithm_time_dict, algo_name_list = self.run_algorithms(algo_list, data_list, item)
        graph_details = {
            'name': f"{', '.join(algo_name_list)} Algorithms time Graph",
            'x_label': 'Algorithms',
            'y_label': 'Time in milliseconds',
            'graph_type': 'line'
        }
        return algorithm_time_dict, graph_details

    @staticmethod
    def choose_input_type():
        """
        This function will give choice to user for input type.
        :return: input type choice.
        """
        while True:
            try:
                return int(input("1. Random Input\n2. User Input\nEnter input type choice: "))
            except ValueError:
                print('Invalid Input Type\n')

    def choose_algorithms(self, no_of_algo=None):
        """
        This function will choose the algorithms for test. For single algorithm test it will allow to choose only
        one algorithm. For multiple algorithm test it will allow to choose multiple algorithms space separated.
        :param no_of_algo: If the chosen test type is single algorithm, the value will be 1 else it will None
        :return: Chosen algorithm/s
        """
        while True:
            try:
                for k, v in self.algo_map.items():
                    print(f"{k}. {v}")

                if no_of_algo == 1:
                    return int(input('Select Algorithm: '))
                else:
                    algo_list = input('Enter algorithms(numbers space separated): ').split()
                    algorithm_list = []
                    for num in algo_list:
                        if 1 > int(num) or int(num) > 4:
                            raise Exception
                        else:
                            algorithm_list.append(int(num))
                    return algorithm_list
            except Exception:
                print('Invalid Input Type\n')

    @staticmethod
    def choose_test_type():
        """
        This function will choose the test type. If the invalid input is given it will again ask to enter input.
        :return: choice. The test choice
        """
        while True:
            try:
                choice = int(input("Select Test Type: \n1. Single Algorithm Test\n2. Multiple Algorithm Test\nEnter "
                                   "your choice: "))
                if choice not in [1, 2]:
                    raise Exception
                return choice
            except Exception:
                print('Invalid Input Type\n')

    @staticmethod
    def generate_random_input():
        """
        This function will generate random input data.
        :return: input_list: list of data
        :return: search_item: Item to be search in input_list.
        """
        input_size = random.randint(0, 100)
        input_list = random.sample(range(0, 100), input_size)
        search_item = random.randint(0, 100)
        return input_list, search_item

    @staticmethod
    def get_user_input():
        """
        This function will take input data from user.
        :return: input_list: list of data
        :return: search_item: Item to be search in input_list.
        """
        while True:
            try:
                input_size = int(input("Enter size of input: "))
                input_list = []
                print("Enter number input: ")
                for i in range(input_size):
                    input_list.append(int(input("Enter number " + str(i + 1) + ": ")))
                search_item = int(input("Enter number to search: "))
                return input_list, search_item
            except ValueError:
                print('Invalid Input Type\n')

    def run_algorithms(self, algo_list, data_list, item):
        """
        This algorithm will run all the chosen algorithms.
        :param algo_list: List of algorithms to execute
        :param data_list: Input data list
        :param item: Item to search
        :return: algo_time_map: Algorithm and time needed to execute them.
        :return: algo_name_list: Names of algorithm used.
        """
        algo_time_map, algo_name_list = ({}, [])
        for algo in algo_list:
            algo_name_list.append(self.algo_map[algo])
            start_time, end_time = self.algo_obj_map[self.algo_map[algo]].get_data(data_list, item)
            algo_time_map[self.algo_map[algo]] = (end_time - start_time) * 1000
        return algo_time_map, algo_name_list

    @staticmethod
    def create_graph(x_y_values, graph_details):
        """
        This function will create the graph for executed test.
        :param x_y_values: Values of x and y axis for graph
        :param graph_details: Graph Details
        :return: None
        """
        if graph_details['graph_type'] == 'line':
            plot_graph.plot(list(x_y_values.keys()), list(x_y_values.values()), marker='.', markerfacecolor='red')
        elif graph_details['graph_type'] == 'bar':
            plot_graph.bar(range(1, len(list(x_y_values.keys())) * 2, 2), list(x_y_values.values()),
                           tick_label=list(x_y_values.keys()),
                           width=0.5)
        plot_graph.xlabel(graph_details['x_label'])
        plot_graph.ylabel(graph_details['y_label'])
        plot_graph.title(graph_details['name'])
        plot_graph.show()


if __name__ == '__main__':
    execute_script_obj = ExecuteScript()
    execute_script_obj.run_script()
