import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) 
 
from models.book import Book 
 
def test_book_creation(): 
    \"\"\"Тест создания книги\"\"\" 
    book = Book("Преступление и наказание", "Ф.М. Достоевский", "123-456", 1866) 
    assert book.title == "Преступление и наказание" 
    assert book.author == "Ф.М. Достоевский" 
    assert book.isbn == "123-456" 
    assert book.publication_year == 1866 
    assert book.is_available == True 
 
def test_book_string_representation(): 
    \"\"\"Тест строкового представления книги\"\"\" 
    book = Book("1984", "Джордж Оруэлл", "789-012", 1949) 
    expected = "'1984' - Джордж Оруэлл (1949) - доступна" 
    assert str(book) == expected 
 
def test_toggle_availability(): 
    \"\"\"Тест изменения доступности книги\"\"\" 
    book = Book("Test Book", "Test Author", "111", 2023) 
    assert book.is_available == True 
    book.toggle_availability() 
    assert book.is_available == False 
    book.toggle_availability() 
    assert book.is_available == True 
