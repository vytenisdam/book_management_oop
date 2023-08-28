from book import Book
from catalog import Catalog
from file_reader import FileReader

is_on = True

while is_on == True:
    
    all = Catalog(FileReader.read_file())
    print('Welcome to Book management system!')
    choice = input('What would you like to do add book(add), remove book(remove), see booklist(see), edit a book(edit)?')
    
    if choice == 'see':
        all.display_books()
        
    elif choice == 'remove':
        name = input('Which book would you like to delete?')
        all.remove_book(name)
        
    elif choice == 'add':
        name = input('What is the name of the book?')
        author = input('What is the author of the book?')
        year = int(input('When was the book released?'))
        quantity = int(input('How many books would you like to add?'))
        all.add_book(name,author,year,quantity)
        
    elif choice == 'edit':
        name = input('What is the name of the book you would like to edit?')
        old_book = all.search_by_name(name)
        all.books.remove(old_book)
        print(f'Here is the old book info: {old_book}')
        new_name = input('Insert new name: ')
        new_author = input('Insert new author: ')
        new_year = int(input('insert new year: '))
        new_quantity = int(input('insert new quantity: '))
        all.add_book(new_name, new_author, new_year, new_quantity)
    
    