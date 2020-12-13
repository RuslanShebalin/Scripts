from typing import List
import decorators

# https://foxford.ru/wiki/informatika/bystraya-sortirovka-hoara


@decorators.timeit
def sort_shell(data: List[int]):
    '''
    Sorting an array using the Shell method

    Args:
        data (List[int]): array with data
    '''
    step = len(data) // 2
    while step > 0:
        for i in range(len(data) - step):
            j = i
            while (j >= 0 and data[j] > data[j + step]):
                data[j], data[j + step] = data[j + step], data[j]
                j -= step
        step //= 2


@decorators.timeit
def sort_hoar(data: List[int]):
    quick_sort(data, 0, len(data) - 1)


@decorators.timeit
def sort_piramid(data: List[int]):
    heapsort(data, 0, len(data) - 1)


@decorators.timeit
def sort_introsort(data: List[int]):
    maxdepth = (len(data).bit_length() - 1) * 2
    introsort_helper(data, 0, len(data) - 1, maxdepth)


def introsort_helper(data: List[int], start: int, end: int, maxdepth: int):
    if end - start <= 0:
        return
    elif maxdepth == 0:
        heapsort(data, start, end)
    else:
        p = partition(data, start, end)
        if (start < p - 1):
            introsort_helper(data, start, p - 1, maxdepth - 1)
        if (p + 1 < end):
            introsort_helper(data, p + 1, end, maxdepth - 1)


def quick_sort(data: List[int], left: int, right: int):
    '''
    Quick sort

    Args:
        data (List[int]): array for sort
        left (int): index of left element
        right (int):  index of right element
    '''
    pivot = partition(data, left, right)
    if (left < pivot - 1):
        quick_sort(data, left, pivot - 1)
    if (pivot + 1 < right):
        quick_sort(data, pivot + 1, right)


def partition(data: List[int], left: int, right: int):
    i = left
    j = right
    # m_index = (i+j+1) // 2
    m_index = right
    while i < j:
        while (data[i] < data[m_index] and i < m_index):
            i += 1
        while (data[j] > data[m_index] and j > m_index):
            j -= 1
        if (i < j):
            swap(data, i, j)
            if j == m_index:
                m_index = i
                j -= 1
            elif (i == m_index):
                m_index = j
                i += 1
            else:
                j -= 1
                i += 1
    # print(f'sort from={left} to {right} pivot {m_index}. {data}')
    return m_index


def swap(data: List[int], i: int, j: int):
    data[i], data[j] = data[j], data[i]


def heapsort(data, start, end):
    build_max_heap(data, start, end + 1)
    for i in range(end, start, -1):
        swap(data, start, i)
        max_heapify(data, index=0, start=start, end=i)


def build_max_heap(data: List[int], start: int, end: int):
    def parent(i):
        return (i-1) // 2

    length = end - start
    index = parent(length)
    while index >= 0:
        max_heapify(data, index, start, end)
        index = index - 1


def max_heapify(data: List[int], index: int, start: int, end: int):
    def left(i):
        return 2*i + 1

    def right(i):
        return 2*i + 2

    size = end - start
    l_node = left(index)
    r_node = right(index)
    if (l_node < size and data[start + l_node] > data[start + index]):
        largest = l_node
    else:
        largest = index
    if (r_node < size and data[start + r_node] > data[start + largest]):
        largest = r_node
    if largest != index:
        swap(data, start + largest, start + index)
        max_heapify(data, largest, start, end)
