import csv

def get_index(data_file):
    index = []
    with open(data_file) as f:
        reader = csv.reader(f)
        for line in reader:
            symbol = line[0]
            index.append(symbol)
    return index



  