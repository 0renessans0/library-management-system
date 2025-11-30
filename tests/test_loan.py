import sys 
import os 
from datetime import datetime, timedelta 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) 
 
from models.loan import Loan 
 
def test_loan_creation(): 
    \"\"\"Тест создания записи о выдаче\"\"\" 
    loan = Loan(1, 100, "ISBN-123") 
    assert loan.loan_id == 1 
    assert loan.user_id == 100 
    assert loan.book_isbn == "ISBN-123" 
    assert loan.return_date is None 
    assert isinstance(loan.borrow_date, datetime) 
    assert isinstance(loan.due_date, datetime) 
 
def test_mark_returned(): 
    \"\"\"Тест отметки о возврате\"\"\" 
    loan = Loan(1, 100, "ISBN-123") 
    assert loan.return_date is None 
    loan.mark_returned() 
    assert loan.return_date is not None 
    assert isinstance(loan.return_date, datetime) 
