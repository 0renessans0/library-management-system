import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) 
 
from models.user import User 
 
def test_user_creation(): 
    user = User(1, "John Doe", "john@example.com") 
    assert user.user_id == 1 
    assert user.name == "John Doe" 
    assert user.email == "john@example.com" 
    assert user.borrowed_books == [] 
 
def test_borrow_and_return_book(): 
    user = User(1, "Test User", "test@test.com") 
 
    assert user.borrow_book("123") == True 
    assert "123" in user.borrowed_books 
 
    assert user.borrow_book("123") == False 
 
    assert user.return_book("123") == True 
    assert "123" not in user.borrowed_books 
 
    assert user.return_book("999") == False 
 
if __name__ == "__main__": 
    test_user_creation() 
    test_borrow_and_return_book() 
    print("All User tests passed!") 
