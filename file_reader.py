import csv

class FileReader:
    
    def __init__(self):
        pass
        
    def read_file():  
        with open('library.csv', 'r', newline = '') as file:
            reader = csv.DictReader(file)
            data = []
            for i in reader:
                data.append(i)
            return data
            
    
    def write_file(data):
        with open('library.csv','w', newline = '') as file:
            fieldnames = ['Book name','Author','Release year','Quantity']
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            for i in data:
                writer.writerow(i)
            
            