import csv, json

def get_json(data_file):
    index = {}
    with open(data_file) as f:
        reader = csv.DictReader(f)
        for line in reader:
            symbol = line['symbol']
            index[symbol] = line

    with open('index.json', 'w') as jsonFile:
      jsonFile.write(json.dumps(index, indent=4))
    
    return(index)
