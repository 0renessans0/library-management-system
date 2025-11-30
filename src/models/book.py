class Book: 
    def __init__(self, title, author, isbn, publication_year): 
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        self.publication_year = publication_year 
        self.is_available = True 
 
    def __str__(self): 
        status = "available" if self.is_available else "borrowed" 
        return f"'{self.title}' - {self.author} ({self.publication_year}) - {status}" 
 
    def toggle_availability(self): 
        self.is_available = not self.is_available 
 
    def get_info(self): 
        return { 
            'title': self.title, 
            'author': self.author, 
            'isbn': self.isbn, 
            'publication_year': self.publication_year, 
            'is_available': self.is_available 
        } 
