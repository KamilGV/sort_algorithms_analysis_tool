from abc import ABC, abstractmethod


class SortAlgorithm(ABC):
    __name = '"Name_Sort_Algorithm"'

    @classmethod
    def get_name(cls):
        return cls.__name

    @staticmethod
    @abstractmethod
    def sorted(values_list: list) -> list:
        pass


