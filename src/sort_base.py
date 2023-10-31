import random
from typing import List, Tuple
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
from .algorithms import SortAlgorithm
import matplotlib.pyplot as plt
import time
# TODO Как назвать этот файл? и класс


class SortBase:
    def __init__(
            self,
            algos: List[SortAlgorithm],
            number_runs: int = 1,
            len_data_list: Tuple = tuple([pow(10, i) for i in range(5)]),

    ):
        self.algos = algos
        self.number_runs = number_runs
        self.len_data_list = len_data_list
        self.results = None

    def show_plot(self):
        if self.results is None:
            raise Exception('Results not found')

        x = list(self.len_data_list)
        x_new = np.linspace(min(x), max(x), 500)

        for i in self.algos:
            y = [res[1] for res in self.results[i]]
            spl = make_interp_spline(x, y, k=3)
            y_new = spl(x_new)
            plt.plot(x_new, y_new, label=i.get_name())
        plt.legend(loc='upper center')

        plt.show()

    def process(self):
        data = self.generate_data()
        results = {}
        for alg in self.algos:
            results[alg] = []
        for alg in self.algos:
            for n in self.len_data_list:
                total_t = 0
                for i in data[n]:
                    t = self.run(alg, i[:])
                    #print(t)
                    total_t += t
                avg = total_t/len(data[n])
                results[alg].append([n, avg])
        print(results)
        self.results = results

    def run(self, alg, data):
        t = time.time()
        sorted_data = alg.sorted(data)
        t = time.time() - t
        if self.check(sorted_data):
            return t
        else:
            raise Exception('Algorithm {} Broken'.format(alg.get_name()))

    def generate_data(self):
        data = {}
        for i in self.len_data_list:
            lists_to_sort = []
            for y in range(self.number_runs):
                lists_to_sort.append(random.sample(range(10**8), i))
            data[i] = lists_to_sort
            print('Сгенерированы')
        return data

    @staticmethod
    def check(list_to_check):
        if list_to_check == sorted(list_to_check):
            return True
        return False
