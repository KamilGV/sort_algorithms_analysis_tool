from .abstract import SortAlgorithm


class PythonSort(SortAlgorithm):
    __name = 'Python_Sort'

    @classmethod
    def get_name(cls):
        return cls.__name

    @staticmethod
    def sorted(values_list: list) -> list:
        return sorted(values_list)


