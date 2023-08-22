from book import Book
from catalog import Catalog
from file_reader import FileReader


#print(FileReader.read_file())
a = Catalog(FileReader.read_file())

a.display_books()
print(a.get_books())