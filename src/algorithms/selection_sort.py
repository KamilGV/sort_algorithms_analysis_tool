from .abstract import SortAlgorithm


class SelectionSort(SortAlgorithm):
    __name = 'Selection_Sort'

    @classmethod
    def get_name(cls):
        return cls.__name

    @staticmethod
    def sorted(values_list: list) -> list:
        for i in range(len(values_list)):
            val = values_list[i]
            index = i
            for y in range(i, len(values_list)):
                if values_list[y] < val:
                    index = y
                    val = values_list[y]
            values_list[i], values_list[index] = values_list[index], values_list[i]
        return values_list







