import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) 
 
from models.user import User 
 
def test_user_creation(): 
    \"\"\"Тест создания пользователя\"\"\" 
    user = User(1, "Иван Петров", "ivan@example.com") 
    assert user.user_id == 1 
    assert user.name == "Иван Петров" 
    assert user.email == "ivan@example.com" 
    assert user.borrowed_books == [] 
 
def test_borrow_and_return_book(): 
    \"\"\"Тест выдачи и возврата книги\"\"\" 
    user = User(1, "Test User", "test@test.com") 
 
    # Тест выдачи книги 
    assert user.borrow_book("123") == True 
    assert "123" in user.borrowed_books 
 
    # Тест повторной выдачи той же книги 
    assert user.borrow_book("123") == False 
 
    # Тест возврата книги 
    assert user.return_book("123") == True 
    assert "123" not in user.borrowed_books 
 
    # Тест возврата несуществующей книги 
    assert user.return_book("999") == False 
