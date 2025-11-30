class User: 
    def __init__(self, user_id, name, email): 
        self.user_id = user_id 
        self.name = name 
        self.email = email 
        self.borrowed_books = [] 
 
    def __str__(self): 
        return f"User: {self.name} (ID: {self.user_id})" 
 
    def borrow_book(self, isbn): 
        if isbn not in self.borrowed_books: 
            self.borrowed_books.append(isbn) 
            return True 
        return False 
 
    def return_book(self, isbn): 
        if isbn in self.borrowed_books: 
            self.borrowed_books.remove(isbn) 
            return True 
        return False 
 
    def get_borrowed_books(self): 
        return self.borrowed_books.copy() 
 
    def get_info(self): 
        return { 
            'user_id': self.user_id, 
            'name': self.name, 
            'email': self.email, 
            'borrowed_books_count': len(self.borrowed_books) 
        } 
