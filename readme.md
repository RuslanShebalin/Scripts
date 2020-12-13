# Использование
## Справка

`python main.py -h`

Результат:
```console
$ python main.py -h
usage: main.py [-h] {sort,gen-samples,graph} ...

Work with sorting algs.

positional arguments:
  {sort,gen-samples,graph}
    sort                Sorting
    gen-samples         Generate sample data
    graph               Route graph



```
## Cотрировка:

### Справка:

```console
python main.py sort -h
```

### Результат:

```console
$ python main.py sort -h
usage: main.py sort [-h] [--alg {shell,hoar,piramid,introsort}] [--input-data-file [INPUT_DATA_FILE [INPUT_DATA_FILE ...]]] [--show-result]

optional arguments:
  -h, --help            show this help message and exit
  --alg {shell,hoar,piramid,introsort}
                        alg for sort
  --input-data-file [INPUT_DATA_FILE [INPUT_DATA_FILE ...]]
                        File with input data
  --show-result         Print result to screen

```
### Пример:

#### один файл:
```console
$ python main.py sort --input-data-file samples/data000.txt --alg shell
Execution time: 0.0004062652587890625
```
####
#### один файл:
```console
$ python main.py sort --input-data-file samples/data000.txt samples/data001.txt samples/data003.txt --alg shell
file = samples/data000.txt
Execution time: 0.00969ms
file = samples/data001.txt
Execution time: 0.01180ms
file = samples/data003.txt
Execution time: 0.00667ms
```
#### несколько файлов с выводом результата на экран:
```console
$ python main.py sort --input-data-file samples/data000.txt samples/data001.txt samples/data003.txt samples/data004.txt samples/data005.txt --alg shell --show-result
file = samples/data000.txt
Execution time: 0.00840ms
unsorted array = [50, -62, -2, -28, -23, -49, -22, -31, 16, -83]
sorted array = [-83, -62, -49, -31, -28, -23, -22, -2, 16, 50]
file = samples/data001.txt
Execution time: 0.00963ms
unsorted array = [-63, -67, 72, 50, 27, 91, 88, -33, -64, 69]
sorted array = [-67, -64, -63, -33, 27, 50, 69, 72, 88, 91]
file = samples/data003.txt
Execution time: 0.01211ms
unsorted array = [-74, -70, -61, 34, 4, 25, -7, 90, -44, 83]
sorted array = [-74, -70, -61, -44, -7, 4, 25, 34, 83, 90]
file = samples/data004.txt
Execution time: 0.00816ms
unsorted array = [5, -10, 41, 34, -11, 19, -30, -92, 30, 42]
sorted array = [-92, -30, -11, -10, 5, 19, 30, 34, 41, 42]
file = samples/data005.txt
Execution time: 0.00892ms
unsorted array = [64, 93, 20, -47, -61, 84, -25, 44, 79, -20]
sorted array = [-61, -47, -25, -20, 20, 44, 64, 79, 84, 93]
```

#### все файлы по шаблону "*.txt" из папки:
```console
$ python main.py sort --input-data-file $(ls samples/*.txt) --alg introsort
file = samples/data000.txt
Execution time: 0.00767ms
file = samples/data001.txt
Execution time: 0.00806ms
file = samples/data003.txt
Execution time: 0.00619ms
file = samples/data004.txt
Execution time: 0.00759ms
file = samples/data005.txt
Execution time: 0.01768ms
```
## Графы

### Справка
```console
$ python main.py graph -h
usage: main.py graph [-h] [--route-type {dsf,bfs}]

optional arguments:
  -h, --help            show this help message and exit
  --route-type {dsf,bfs}
                        Type of route graph
```
### Пример
```console
$ python main.py graph --route-type dsf
route: 0->1, visited=[0]
route: 1->2, visited=[0, 1]
route: 2->3, visited=[0, 1, 2]
route: 3->4, visited=[0, 1, 2, 3]
route: 4->5, visited=[0, 1, 2, 3, 4]
route: 5->6, visited=[0, 1, 2, 3, 4, 5]
route: 6->7, visited=[0, 1, 2, 3, 4, 5, 6]
route: 0->8, visited=[0, 1, 2, 3, 4, 5, 6, 7]
route: 8->9, visited=[0, 1, 2, 3, 4, 5, 6, 7, 8]
```
## Генерация набора тестовых данных

### Справка
```console
$ python main.py gen-samples -h
usage: main.py gen-samples [-h] (--filename FILENAME | --dir DIR) [--count COUNT] [--name-template NAME_TEMPLATE] [--min MIN] [--max MAX] [--count-elements COUNT_ELEMENTS]

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME   Generate one sample file
  --dir DIR             Generate multiple sample files

Multiple samples:
  --count COUNT         Count sample files
  --name-template NAME_TEMPLATE
                        Template for file name

Sample setup:
  --min MIN             Minimal value. Default = -100
  --max MAX             Maximum value. Default = 100
  --count-elements COUNT_ELEMENTS
                        Count elements in array. Default = 200
```
### Пример
#### Генерация одного файла
Создается один файл с массивом состоящим из 1000 элементов, минимальное значение элемента -200, максимальное значение элемента 200:

```console
$ python main.py gen-samples --filename sample/test_data.txt --min -200 --max 200 --count-elements 1000
$ ls samples/
test_data.txt
```

#### Генерация нескольких файлов

```console
$ python main.py gen-samples --dir samples/ --count 10
$ ls samples/
data000.txt  data001.txt  data002.txt  data003.txt  data004.txt  data005.txt  data006.txt  data007.txt  data008.txt  data009.txt
```

