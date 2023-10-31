from src.sort_base import SortBase
from src.algorithms import *

if __name__ == '__main__':
    list_of_algorithms = [
        SelectionSort,
        BabbleSort,
        PythonSort,
    ]
    x = SortBase(
        algos=list_of_algorithms,
        number_runs=10,
        len_data_list=tuple([i for i in range(1000, 10000, 1000)])
    )
    x.process()
    x.show_plot()
