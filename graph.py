# https://habr.com/ru/post/112421/
# https://habrastorage.org/storage/107409b2/1e276dc0/8816a7ae/7599c3ea.png
from typing import List

a, b, c, d, e, f, g, h, i, j = range(10)
N = [
    [b, c, d, e, f, i],  # a
    [c, e],  # b
    [d],  # c
    [e],  # d
    [f],  # e
    [c, g, h],  # f
    [f, h],  # g
    [f, g],  # h
    [j],  # i
    []  # j
    ]


def dsf(graph: List[List[int]],
        start_node: int = 0,
        distanation_node: int = -1,
        visited_list: List[int] = []):
    '''
    Depth-first traversal

    Args:
        graph (List[List[int]]): Connectivity List
        start_node (int, optional): Start node. Defaults to 0.
        distanation_node (int, optional): Distanation node. Defaults to -1, traversing the whole graph.
        visited_list (List[int], optional): [description]. Defaults to [].
    '''
    if start_node == distanation_node:
        return True
    if start_node in visited_list:
        return False
    visited_list.append(start_node)

    for neighbor in graph[start_node]:
        if not (neighbor in visited_list):
            print(f'route: {start_node}->{neighbor}, visited={visited_list}')
            reached = dsf(graph, neighbor, distanation_node, visited_list)
            if reached:
                return True
    return False


def bfs(graph: List[List[int]],
        start_node: int = 0,
        distanation_node: int = -1):
    '''
    Width graph traversal

    Args:
        graph (List[List[int]]): Connectivity List
        start_node (int, optional): Start node. Defaults to 0.
        distanation_node (int, optional): Distanation node. Defaults to -1, traversing the whole graph.
    '''
    queue = []
    visited_list = []
    queue.append(start_node)
    visited_list.append(start_node)
    while queue:
        current = queue.pop()
        for neighbor in graph[current]:
            if not (neighbor in visited_list):
                queue.append(neighbor)
                visited_list.append(neighbor)
                print(f'route {current}->{neighbor}')
                if neighbor == distanation_node:
                    return True
    return False
