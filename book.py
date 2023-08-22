class Book:
    
    def __init__(self,name, author, year, quantity):
        self.name = name
        self.author = author
        self.year = year
        self.quantity = quantity
        
    def get_name(self):
        return self.name
    
    def get_author(self):
        return self.author
    
    def get_year(self):
        return self.year
    
    def get_quantity(self):
        return self.quantity
    
    def change_quantity(self, amount):
        self.quanity = amount
    
    def add_books(self, amount):
        self.quantity += amount
        
    def take_books(self, amount):
        self.quantity -= amount
        
    def set_author(self, new):
        self.author = new
        
    def set_name(self, new):
        self.name = new
        
    def set_year(self, new):
        self.year = new
        
