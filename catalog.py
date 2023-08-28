from book import Book
from file_reader import FileReader

books = FileReader.read_file() 

class Catalog:
    
    def __init__(self, books):
        self.books = books
        
    def get_books(self):
        return self.books
    
    def display_books(self):
        for i in self.books:
            print(i)
    
    def search_by_name(self, name):
        for i in FileReader.read_file():
            if i['Book name'] == name:
                return i
            
    def search_by_author(self, author):
        pass
    
    def add_book(self,name, author, year, quantity):
        a = Book(name,author,year,quantity)
        name = a.get_name()
        author = a.get_author()
        year = a.get_year()
        quantity = a.get_quantity()
        books.append({'Book name': name,'Author': author,'Release year': year,'Quantity': quantity})
        print(f'Book named {name}, was added.')
        FileReader.write_file(books)
    
    def remove_book(self, name):
        for i in FileReader.read_file():
            if i['Book name'] == name:
                books.remove(i)
                print(f'Book named {name}, deleted.')
        FileReader.write_file(data = books)

