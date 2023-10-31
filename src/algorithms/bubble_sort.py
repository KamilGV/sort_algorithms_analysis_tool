from .abstract import SortAlgorithm


class BabbleSort(SortAlgorithm):
    __name = 'Bubble_Sort'

    @classmethod
    def get_name(cls):
        return cls.__name

    @staticmethod
    def sorted(values_list: list) -> list:
        bool_change = True
        while bool_change:
            bool_change = False
            for i in range(len(values_list) - 1):
                if values_list[i] > values_list[i+1]:
                    values_list[i], values_list[i+1] = values_list[i+1], values_list[i]
                    bool_change = True
        return values_list
