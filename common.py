import io
import random
import argparse
import graph
from typing import Union, List


def generate_samples_files_batch(count: int = 1,
                                 path: str = '',
                                 name_template: str = 'data',
                                 min_value: int = -100,
                                 max_value: int = 100,
                                 count_elements: int = 200):
    '''
    generating group of files with examples

    Args:
        count (int, optional): Number of files to create. Defaults to 1.
        path (str, optional):path to folder for files. Defaults to current folder.
        name_template (str, optional): Template for filename (data001.txt). Defaults to 'data'.
        min_value (int, optional): Minimum value of element in array. Defaults to -100.
        max_value (int, optional): Maximum value of element in array. Defaults to 100.
        count_elements (int, optional): Count of elements in array. Defaults to 200.
    '''
    for i in range(count):
        with open(f'{path}/{name_template}{i:003}.txt', 'w') as file:
            sample_list = [
                random.randint(min_value,
                               max_value) for _ in range(count_elements)
            ]
            file.write(' '.join(str(item) for item in sample_list))


def generate_sample_file(filename: str,
                         min_value: int = -100,
                         max_value: int = 100,
                         count_elements: int = 200) -> None:
    '''
    generating a file with examples

    Args:
        filename (str): filename with path
        min_value (int, optional): Minimum value of element in array. Defaults to -100.
        max_value (int, optional): Maximum value of element in array. Defaults to 100.
        count_elements (int, optional): Count of elements in array. Defaults to 200.
    '''
    with open(filename, 'w') as file:
        sample_list = [
            random.randint(min_value,
                           max_value) for _ in range(count_elements)
        ]
        file.write(' '.join(str(item) for item in sample_list))


def read_list_from_file(filename: Union[str, io.TextIOBase]) -> List[int]:
    '''
    Read array from file

    Args:
        filename (Union[str, io.TextIOBase]): filename or File object

    Returns:
        List[int]: Array with data
    '''
    if isinstance(filename, str):
        file = open(filename, 'r')
    elif isinstance(filename, io.TextIOBase):
        file = filename

    res = file.read()
    lst = [int(s) for s in res.split(' ')]
    return lst


def write_list_to_file(filename: Union[str,
                                       io.TextIOBase],
                       data: List[int]) -> None:
    '''
    Write array to file

    Args:
        filename (Union[str, io.TextIOBase]): filename or File object
        data (List[int]): data array
    '''
    if isinstance(filename, str):
        file = open(filename, 'w')
    elif isinstance(filename, io.TextIOBase):
        file = filename
    file.write(' '.join(str(item) for item in data))
