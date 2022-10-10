from os import path
import re
import string

class FileTypeException(Exception):
    pass

class FilePathException(Exception):
    pass

class MapReduce_Wordcount():
    
    def __init__(self, data_file, output_file):
        if data_file.endswith('.txt') == False:
            raise FileTypeException('You need to give a data txt file')
        if output_file.endswith('.txt') == False:
            raise FileTypeException('You need to give a output txt file')
        if path.isfile(data_file) == False:
            raise FilePathException('Provide correct path of data txt file')
        self.data_file = data_file
        self.output_file = output_file
        self.data = []
        self.mapper_data = []
        self.sorted_data = []
        self.reducer_data = []
    
    def record_reader(self):
        data = []
        with open(self.data_file) as f:
            y = f.read()
            for character in string.punctuation:
                y = y.replace(character, '')
            print(y)
            self.data = y.split()
        return self.data
    
    def mapper(self):
        for i in self.data:
            self.mapper_data.append({i:1})
        return self.mapper_data
    
    def sorter(self):
        x = []
        for i in self.mapper_data:
            for key, value in i.items():
                x.append(key)
        x = sorted(list(set(x)))
        print(x)
        for i in x:
            for j in self.mapper_data:
                for key, value in j.items():
                    k = key
                if i == k:
                    self.sorted_data.append(j)
        return self.sorted_data
    
    def reducer(self):
        x = []
        for i in self.mapper_data:
            for key, value in i.items():
                x.append(key)
        x = sorted(list(set(x)))
        z = []
        for i in x:
            l = 0
            for j in self.sorted_data:
                for key, value in j.items():
                    k = key
                if i == k:
                    l += 1
            self.reducer_data.append((i, l))
        return self.reducer_data
    
    def record_writer(self):
        for i in range(len(self.reducer_data)):
            self.reducer_data[i] = list(self.reducer_data[i])
        with open(self.output_file, 'w+', newline = '') as f:
            for x in self.reducer_data:
                f.writelines(f'{str(x[0])} {str(x[1])}\n')
        return f'File {self.output_file} written successfully'