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
        # FileReader.read_file()
        # for i in books:
        #     print(Book.get_name(i), Book.get_author(i), Book.get_year(i), Book.get_quantity(i))
    
    def search_by_name():
        #new_data = []
        for i in FileReader.read_file():
            print(i)
        # for i in new_data:
        #     print(i)
            # if i['Book name'] == name:
            #     print(i)
            
    def search_by_author(self, author):
        pass
    
    def add_book(self, name, author, year, quantity):
        a = Book(name,author,year,quantity)
        books.append(a)
        FileReader.write_file(books)
    
    def remove_book(self, name, author, year):
        pass
    
Catalog.add_book()