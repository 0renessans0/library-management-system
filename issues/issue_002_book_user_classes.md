# Issue #002: Реализация классов Book и User 
 
## Задача: 
Реализовать базовые классы Book и User 
 
## Требования к классу Book: 
- Атрибуты: title, author, isbn, publication_year, is_available 
- Методы: __init__, __str__, toggle_availability, get_info 
 
## Требования к классу User: 
- Атрибуты: user_id, name, email, borrowed_books 
- Методы: __init__, __str__, borrow_book, return_book, get_borrowed_books 
 
## Критерии выполнения: 
- [ ] Реализован класс Book в src/models/book.py 
- [ ] Реализован класс User в src/models/user.py 
- [ ] Написаны тесты в tests/test_book.py и tests/test_user.py 
