import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) 
 
from models.book import Book 
 
def test_book_creation(): 
    book = Book("Test Book", "Test Author", "123-456", 2023) 
    assert book.title == "Test Book" 
    assert book.author == "Test Author" 
    assert book.isbn == "123-456" 
    assert book.publication_year == 2023 
    assert book.is_available == True 
 
def test_book_string_representation(): 
    book = Book("1984", "George Orwell", "789-012", 1949) 
    expected = "'1984' - George Orwell (1949) - available" 
    assert str(book) == expected 
 
def test_toggle_availability(): 
    book = Book("Test Book", "Test Author", "111", 2023) 
    assert book.is_available == True 
    book.toggle_availability() 
    assert book.is_available == False 
    book.toggle_availability() 
    assert book.is_available == True 
 
if __name__ == "__main__": 
    test_book_creation() 
    test_book_string_representation() 
    test_toggle_availability() 
    print("All Book tests passed!") 
