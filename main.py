import argparse
import os

import common
import graph
import sorting


def addParser():
    parser = argparse.ArgumentParser(description='Work with sorting algs.')
    parser.set_defaults(type=None)
    subparsers = parser.add_subparsers()

    parser_sort = subparsers.add_parser('sort', help='Sorting')
    add_parser_sort(parser_sort)

    parser_graph = subparsers.add_parser('graph', help='Route graph')
    add_parser_graph(parser_graph)

    parser_gen_samples = subparsers.add_parser('gen-samples',
                                               help='Generate sample data')
    add_parser_gen_sample(parser_gen_samples)

    return parser


def add_parser_sort(parser: argparse.ArgumentParser):
    parser.set_defaults(type='sort')
    parser.add_argument(
        '--alg',
        # required=True,
        help='alg for sort',
        choices=['shell',
                 'hoar',
                 'piramid',
                 'introsort'])
    parser.add_argument('--input-data-file',
                        help='File with input data',
                        nargs='*',
                        type=argparse.FileType('r'),
                        required=True)
    parser.add_argument('--show-result',
                        help='Print result to screen',
                        action='store_true')


def add_parser_gen_sample(parser: argparse.ArgumentParser):
    parser.set_defaults(type='gen-sample')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--filename', help='Generate one sample file')
    group.add_argument('--dir', help='Generate multiple sample files')

    group_mul = parser.add_argument_group('Multiple samples')
    group_mul.add_argument('--count',
                           help='Count sample files',
                           default=1,
                           type=int)
    group_mul.add_argument('--name-template',
                           help='Template for file name',
                           default='data')

    group_sample_setup = parser.add_argument_group('Sample setup')
    group_sample_setup.add_argument('--min',
                                    help='Minimal value. Default = -100',
                                    type=int,
                                    default=-100)
    group_sample_setup.add_argument('--max',
                                    help='Maximum value. Default = 100',
                                    type=int,
                                    default=100)
    group_sample_setup.add_argument(
        '--count-elements',
        help='Count elements in array. Default = 200',
        type=int,
        default=200)


def add_parser_graph(parser: argparse.ArgumentParser):
    parser.set_defaults(type='graph')
    parser.add_argument('--route-type',
                        choices=['dsf',
                                 'bfs'],
                        help='Type of route graph')


def parse_args_sort(args):
    if not args.alg:
        print('Nothing to do. Choose algorithm')
        return

    for f in args.input_data_file:
        array = common.read_list_from_file(f)
        print(f'file = {f.name}')
        copy_array = array.copy()
        copy_array_unsorted = array.copy()
        copy_array.sort()
        if args.alg == 'shell':
            sorting.sort_shell(array)
        if args.alg == 'hoar':
            sorting.sort_hoar(array)
        if args.alg == 'piramid':
            sorting.sort_piramid(array)
        if args.alg == 'introsort':
            sorting.sort_introsort(array)

        if array != copy_array:
            print(f'FAIL path={f}')
        file_to_write = os.path.join(os.path.dirname(f.name),
                                     f'{os.path.basename(f.name)}.out')
        common.write_list_to_file(file_to_write, array)
        if args.show_result:
            print(f'unsorted array = {copy_array_unsorted}')
            print(f'sorted array = {array}')


def parse_args_gen_sample(args):

    if args.filename:
        common.generate_sample_file(args.filename,
                                    args.min,
                                    args.max,
                                    args.count_elements)
    elif args.dir:
        common.generate_samples_files_batch(args.count,
                                            args.dir,
                                            args.name_template,
                                            args.min,
                                            args.max,
                                            args.count_elements)


def parse_args_graph(args):
    if args.route_type == 'dsf':
        graph.dsf(graph.N, 0, 1000)
    elif args.route_type == 'bfs':
        graph.bfs(graph.N, 0, 1000)
    else:
        print('Unknown type of route')


def main(parser):

    args = parser.parse_args()
    if args and args.type == 'gen-sample':
        parse_args_gen_sample(args)
    elif args and args.type == 'graph':
        parse_args_graph(args)
    elif args.type == 'sort':
        parse_args_sort(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    parser = addParser()
    main(parser)
