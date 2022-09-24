# Implementation of Hadoop Mapreduce on Local Text files

## Installing the Library
```
pip install hadoop_mapreduce
```

## Classes available in this Library
1. MapReduce_Maximum - Find maximum values of the keys available
2. MapReduce_Minimum - Find minimum values of the keys available

## MapReduce_Maximum
### Importing
```
from hadoop_mapreduce import MapReduce_Maximum
```
### Calling the class
```
data = MapReduce_Maximum(<path to text file>, <path to text meta file>, <path to output file>)
```
`text file` should contain records of the data. Example:
```
Hola,2,3,4
Hello,6,7,8
Hi,10,11,12
Hello,1,3,4
Hi,1,5,3
Hola,1,10,20
```
`meta file` should contain the column names of the file. Example:
```
A,B,C,D
```
`output file` will be created at the end of mapreduce implementation
### Record Reader
Code:
```
data.record_reader()
```
Output:
```
[{'A': 'Hola', 'B': 2.0, 'C': 3.0, 'D': 4.0},
 {'A': 'Hello', 'B': 6.0, 'C': 7.0, 'D': 8.0},
 {'A': 'Hi', 'B': 10.0, 'C': 11.0, 'D': 12.0},
 {'A': 'Hello', 'B': 1.0, 'C': 3.0, 'D': 4.0},
 {'A': 'Hi', 'B': 1.0, 'C': 5.0, 'D': 3.0},
 {'A': 'Hola', 'B': 1.0, 'C': 10.0, 'D': 20.0}]
```
### Mapper
Code:
```
data.mapper()
```
Output:
```
[('Hola', 4.0),
 ('Hello', 8.0),
 ('Hi', 12.0),
 ('Hello', 4.0),
 ('Hi', 5.0),
 ('Hola', 20.0)]
```
### Sorter & Shuffler
Code:
```
data.sorter()
```
Output:
```
[('Hello', 8.0),
 ('Hello', 4.0),
 ('Hola', 4.0),
 ('Hola', 20.0),
 ('Hi', 12.0),
 ('Hi', 5.0)]
```
### Reducer
Code:
```
data.reducer()
```
Output:
```
[('Hello', 8.0), ('Hola', 20.0), ('Hi', 12.0)]
```
#### Record Writer
Code:
```
data.record_writer()
```
Output:
```
'File <path to output file> written successfully'
```
`output file` has key and highest value of the key. Example:
```
Hello 8.0
Hola 20.0
Hi 12.0
```

## MapReduce_Minimum
### Importing
```
from hadoop_mapreduce import MapReduce_Minimum
```
### Calling the class
```
data = MapReduce_Minimum(<path to text file>, <path to text meta file>, <path to output file>)
```
`text file` should contain records of the data. Example:
```
Hola,2,3,4
Hello,6,7,8
Hi,10,11,12
Hello,1,3,4
Hi,1,5,3
Hola,1,10,20
```
`meta file` should contain the column names of the file. Example:
```
A,B,C,D
```
`output file` will be created at the end of mapreduce implementation
### Record Reader
Code:
```
data.record_reader()
```
Output:
```
[{'A': 'Hola', 'B': 2.0, 'C': 3.0, 'D': 4.0},
 {'A': 'Hello', 'B': 6.0, 'C': 7.0, 'D': 8.0},
 {'A': 'Hi', 'B': 10.0, 'C': 11.0, 'D': 12.0},
 {'A': 'Hello', 'B': 1.0, 'C': 3.0, 'D': 4.0},
 {'A': 'Hi', 'B': 1.0, 'C': 5.0, 'D': 3.0},
 {'A': 'Hola', 'B': 1.0, 'C': 10.0, 'D': 20.0}]
```
### Mapper
Code:
```
data.mapper()
```
Output:
```
[('Hola', 4.0),
 ('Hello', 8.0),
 ('Hi', 12.0),
 ('Hello', 4.0),
 ('Hi', 5.0),
 ('Hola', 20.0)]
```
### Sorter & Shuffler
Code:
```
data.sorter()
```
Output:
```
[('Hello', 8.0),
 ('Hello', 4.0),
 ('Hola', 4.0),
 ('Hola', 20.0),
 ('Hi', 12.0),
 ('Hi', 5.0)]
```
### Reducer
Code:
```
data.reducer()
```
Output:
```
[('Hello', 1.0), ('Hola', 1.0), ('Hi', 1.0)]

```
#### Record Writer
Code:
```
data.record_writer()
```
Output:
```
'File <path to output file> written successfully'
```
`output file` has key and highest value of the key. Example:
```
Hello 1.0
Hola 1.0
Hi 1.0
```
