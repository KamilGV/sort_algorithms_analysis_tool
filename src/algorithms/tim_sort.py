from .abstract import SortAlgorithm


class TimSort(SortAlgorithm):
    __name = 'Tim_Sort'

    @classmethod
    def get_name(cls):
        return cls.__name

    @classmethod
    def sorted(cls, values_list: list) -> list:
        min_run = cls.calc_min_run(len(values_list))
        runs = cls.find_runs(values_list, min_run)

        return []

    @classmethod
    def calc_min_run(cls, n: int) -> int:
        r = 0
        while n >= 64:
            r |= n & 1
            n >>= 1
        return n+r

    @classmethod
    def find_runs(cls, arr: list[int], min_run: int) -> list[list[int]]:
        return_list = []
        # нужен флаг на порядок сортировки ASС = TRUE
        n = len(arr)
        i = 0
        pass





    @classmethod
    def reverse_list(cls, arr: list) -> list:
        for i in range(len(arr)//2):
            arr[i], arr[-i-1] = arr[-i-1], arr[i]
        return arr

    @classmethod
    def insertion_sort(cls, arr: list) -> list:
        for i in range(1, len(arr)):
            key = arr[i]

            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1
        return arr

    @classmethod
    def binary_search(cls, arr: list, elem: int) -> int | None:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == elem:
                return m
            elif arr[m] > elem:
                r = m - 1
            else:
                l = m + 1
        return None

    #Пока обычная сортировка слиянием
    #А тут не простой бинарный поиск, он аля за ту же скорость,
    @classmethod
    def merge(cls, arr1: list, arr2: list) -> list:
        return_list = []
        index_1 = 0
        index_2 = 0
        while index_1 < len(arr1) and index_2 < len(arr2):
            if arr1[index_1] < arr2[index_2]:
                return_list.append(arr1[index_1])
                index_1 += 1
            else:
                return_list.append(arr2[index_2])
                index_2 += 1
        if index_1 >= len(arr1):
            return_list.extend(arr2[index_2:])
        else:
            return_list.extend(arr1[index_1:])
        return return_list



