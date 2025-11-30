from datetime import datetime, timedelta 
 
class Loan: 
    def __init__(self, loan_id, user_id, book_isbn, borrow_days=14): 
        self.loan_id = loan_id 
        self.user_id = user_id 
        self.book_isbn = book_isbn 
        self.borrow_date = datetime.now() 
        self.due_date = self.borrow_date + timedelta(days=borrow_days) 
        self.return_date = None 
 
    def mark_returned(self): 
        self.return_date = datetime.now() 
 
    def is_overdue(self): 
        if self.return_date: 
            return self.return_date 
        return datetime.now() 
 
    def get_info(self): 
        return { 
            'loan_id': self.loan_id, 
            'user_id': self.user_id, 
            'book_isbn': self.book_isbn, 
            'borrow_date': self.borrow_date.strftime("%Y-%m-%d"), 
            'due_date': self.due_date.strftime("%Y-%m-%d"), 
            'return_date': self.return_date.strftime("%Y-%m-%d") if self.return_date else None, 
            'is_overdue': self.is_overdue() 
        } 
