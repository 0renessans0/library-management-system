# UML Диаграмма классов системы управления библиотекой 
 
## Описание диаграммы 
 
### Класс Book 
- **Атрибуты:** title, author, isbn, publication_year, is_available 
- **Методы:** __init__, __str__, toggle_availability, get_info 
 
### Класс User 
- **Атрибуты:** user_id, name, email, borrowed_books 
- **Методы:** __init__, __str__, borrow_book, return_book, get_borrowed_books, get_info 
 
### Класс Loan 
- **Атрибуты:** loan_id, user_id, book_isbn, borrow_date, due_date, return_date 
- **Методы:** __init__, mark_returned, is_overdue, get_info 
 
### Класс Library 
- **Атрибуты:** books, users, loans, next_loan_id 
- **Методы:** add_book, remove_book, register_user, find_book_by_title, find_book_by_author, borrow_book, return_book, get_available_books, get_overdue_loans 
 
## Отношения между классами 
- Library "содержит" множество Book (агрегация) 
- Library "содержит" множество User (агрегация) 
- Library "содержит" множество Loan (композиция) 
- Loan "связан" с одним User (ассоциация) 
- Loan "связан" с одной Book (ассоциация) 
