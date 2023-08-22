import csv

with open ('library.csv' , 'w', newline = '') as file:
    fieldnames = ['Book name', 'Author', 'Release year', 'Quantity']
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    
    writer.writeheader()