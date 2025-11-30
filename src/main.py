import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
 
from src.services.library import Library 
from src.models.book import Book 
from src.models.user import User 
 
def initialize_sample_data(library): 
    books_data = [ 
        ("Crime and Punishment", "Fyodor Dostoevsky", "978-123", 1866), 
        ("1984", "George Orwell", "978-456", 1949), 
        ("Master and Margarita", "Mikhail Bulgakov", "978-789", 1967), 
        ("War and Peace", "Leo Tolstoy", "978-012", 1869), 
        ("Anna Karenina", "Leo Tolstoy", "978-345", 1877) 
    ] 
 
    for title, author, isbn, year in books_data: 
        book = Book(title, author, isbn, year) 
        library.add_book(book) 
 
    users_data = [ 
        (1, "John Smith", "john@example.com"), 
        (2, "Maria Garcia", "maria@example.com"), 
        (3, "Alex Johnson", "alex@example.com") 
    ] 
 
    for user_id, name, email in users_data: 
        user = User(user_id, name, email) 
        library.register_user(user) 
 
def display_library_info(library): 
    print("=== LIBRARY MANAGEMENT SYSTEM ===") 
    print(f"Total books: {len(library.books)}") 
    print(f"Registered users: {len(library.users)}") 
 
    available_books = library.get_available_books() 
    print(f"\nAvailable books ({len(available_books)}):") 
    for book in available_books: 
        print(f"  - {book}") 
 
    print("\nRegistered users:") 
    for user in library.users.values(): 
        print(f"  - {user}") 
 
def demonstrate_functionality(library): 
    print("\n=== FUNCTIONALITY DEMONSTRATION ===") 
 
    print("\n1. Borrowing a book for John Smith:") 
    if library.borrow_book(1, "978-123"): 
        print("   Book 'Crime and Punishment' successfully borrowed!") 
    else: 
        print("   Error borrowing book") 
 
    print("\n2. Searching for books by Tolstoy:") 
    tolstoy_books = library.find_book_by_author("Tolstoy") 
    for book in tolstoy_books: 
        print(f"   - {book}") 
 
    overdue_loans = library.get_overdue_loans() 
    print(f"\n3. Overdue loans: {len(overdue_loans)}") 
 
def main(): 
    library = Library() 
 
    initialize_sample_data(library) 
 
    display_library_info(library) 
 
    demonstrate_functionality(library) 
 
    print("\n=== PROGRAM COMPLETED ===") 
 
if __name__ == "__main__": 
    main() 
