from typing import Dict, List, Optional 
from ..models.book import Book 
from ..models.user import User 
from ..models.loan import Loan 
 
class Library: 
    """Основной класс для управления библиотекой""" 
 
    def __init__(self): 
        self.books: Dict[str, Book] = {}  # ISBN -
        self.users: Dict[int, User] = {}  # user_id -
        self.loans: List[Loan] = [] 
        self.next_loan_id = 1 
 
    def add_book(self, book: Book) -
        """Добавить книгу в библиотеку""" 
        if book.isbn in self.books: 
            return False 
        self.books[book.isbn] = book 
        return True 
 
    def remove_book(self, isbn: str) -
        """Удалить книгу из библиотеки""" 
        if isbn in self.books: 
            del self.books[isbn] 
            return True 
        return False 
 
    def register_user(self, user: User) -
        """Зарегистрировать пользователя""" 
        if user.user_id in self.users: 
            return False 
        self.users[user.user_id] = user 
        return True 
 
    def find_book_by_title(self, title: str) -
        """Найти книги по названию""" 
        return [book for book in self.books.values() if title.lower() in book.title.lower()] 
 
    def find_book_by_author(self, author: str) -
        """Найти книги по автору""" 
        return [book for book in self.books.values() if author.lower() in book.author.lower()] 
 
    def borrow_book(self, user_id: int, isbn: str) -
        """Выдать книгу пользователю""" 
        if user_id not in self.users or isbn not in self.books: 
            return False 
 
        user = self.users[user_id] 
        book = self.books[isbn] 
 
        if not book.is_available: 
            return False 
 
        loan = Loan(self.next_loan_id, user_id, isbn) 
        self.loans.append(loan) 
        self.next_loan_id += 1 
 
        book.toggle_availability() 
        user.borrow_book(isbn) 
 
        return True 
 
    def return_book(self, user_id: int, isbn: str) -
        """Принять возврат книги""" 
        if user_id not in self.users or isbn not in self.books: 
            return False 
 
        user = self.users[user_id] 
        book = self.books[isbn] 
 
        active_loan = None 
        for loan in self.loans: 
            if (loan.user_id == user_id and loan.book_isbn == isbn and loan.return_date is None): 
                active_loan = loan 
                break 
 
        if not active_loan: 
            return False 
 
        active_loan.mark_returned() 
        book.toggle_availability() 
        user.return_book(isbn) 
 
        return True 
 
    def get_available_books(self) -
        """Получить список доступных книг""" 
        return [book for book in self.books.values() if book.is_available] 
 
    def get_overdue_loans(self) -
        """Получить список просроченных выдач""" 
        return [loan for loan in self.loans if loan.is_overdue() and loan.return_date is None] 
 
    def get_user_loans(self, user_id: int) -
        """Получить список выдач пользователя""" 
        return [loan for loan in self.loans if loan.user_id == user_id] 
