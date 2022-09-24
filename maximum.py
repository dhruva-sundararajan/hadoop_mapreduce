from os import path

class FileTypeException(Exception):
    pass

class FilePathException(Exception):
    pass

class MapReduce_Maximum():
    
    def __init__(self, data_file, meta_file, output_file):
        if data_file.endswith('.txt') == False:
            raise FileTypeException('You need to give a data txt file')
        if meta_file.endswith('.txt') == False:
            raise FileTypeException('You need to give a meta txt file')
        if output_file.endswith('.txt') == False:
            raise FileTypeException('You need to give a output txt file')
        if path.isfile(data_file) == False:
            raise FilePathException('Provide correct path of data txt file')
        if path.isfile(meta_file) == False:
            raise FilePathException('Provide correct path of meta txt file')
        self.data_file = data_file
        self.meta_file = meta_file
        self.output_file = output_file
        self.meta = []
        self.data = []
        self.mapper_data = []
        self.sorted_data = []
        self.reducer_data = []
    
    def record_reader(self):
        with open(self.meta_file) as f:
            meta = f.read().split(',')
        self.meta = meta
        data = []
        with open(self.data_file) as f:
            y = 0
            for line in f:
                locals()[f'd{y}'] = {}
                data_1 = line.split(',')
                for i in range(len(data_1)):
                    if data_1[i].endswith('\n'):
                        data_1[i] = data_1[i].strip()
                    try:
                        data_1[i] = float(data_1[i])
                    except Exception:
                        pass
                for i in range(len(meta)):
                    locals()[f'd{y}'][meta[i]] = data_1[i]
                data.append(locals()[f'd{y}'])
                y += 1
        self.data = data
        return self.data
    
    def mapper(self):
        for i in self.data:
            if type(i) != dict:
                raise DataTypeException('You need to give a dict for each tuple in data')
            x = i['A']
            y = []
            for j in i:
                if type(i[j]) == str:
                    pass
                else:
                    y.append(i[j])
            y = max(y)
            self.mapper_data.append((x, y))
        return self.mapper_data
    
    def sorter(self):
        x = []
        for i in self.mapper_data:
            x.append(i[0])
        x = list(set(sorted(x)))
        for i in x:
            for j in self.mapper_data:
                if i == j[0]:
                    self.sorted_data.append(j)
        return self.sorted_data
    
    def reducer(self):
        x = []
        for i in self.mapper_data:
            x.append(i[0])
        x = list(set(sorted(x)))
        z = []
        for i in x:
            y = []
            for j in self.sorted_data:
                if i == j[0]:
                    y.append(j)
            self.reducer_data.append((y[0][0], max([k[1] for k in y])))
        return self.reducer_data
    
    def record_writer(self):
        for i in range(len(self.reducer_data)):
            self.reducer_data[i] = list(self.reducer_data[i])
        with open(self.output_file, 'w+', newline = '') as f:
            for x in self.reducer_data:
                f.writelines(f'{str(x[0])} {str(x[1])}\n')
        return f'File {self.output_file} written successfully'
