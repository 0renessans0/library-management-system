import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) 
 
from services.library import Library 
from models.book import Book 
from models.user import User 
 
def test_library_initialization(): 
    \"\"\"Тест инициализации библиотеки\"\"\" 
    library = Library() 
    assert len(library.books) == 0 
    assert len(library.users) == 0 
    assert len(library.loans) == 0 
    assert library.next_loan_id == 1 
 
def test_add_and_remove_book(): 
    \"\"\"Тест добавления и удаления книги\"\"\" 
    library = Library() 
    book = Book("Test Book", "Test Author", "123", 2023) 
 
    # Добавление книги 
    assert library.add_book(book) == True 
    assert "123" in library.books 
    assert len(library.books) == 1 
 
    # Добавление дубликата 
    assert library.add_book(book) == False 
 
    # Удаление книги 
    assert library.remove_book("123") == True 
    assert len(library.books) == 0 
 
    # Удаление несуществующей книги 
    assert library.remove_book("999") == False 
 
def test_borrow_and_return_book(): 
    \"\"\"Тест выдачи и возврата книги\"\"\" 
    library = Library() 
 
    # Создание тестовых данных 
    book = Book("Test Book", "Author", "123", 2023) 
    user = User(1, "Test User", "test@test.com") 
 
    library.add_book(book) 
    library.register_user(user) 
 
    # Тест выдачи книги 
    assert library.borrow_book(1, "123") == True 
    assert book.is_available == False 
    assert "123" in user.borrowed_books 
    assert len(library.loans) == 1 
 
    # Тест возврата книги 
    assert library.return_book(1, "123") == True 
    assert book.is_available == True 
    assert "123" not in user.borrowed_books 
