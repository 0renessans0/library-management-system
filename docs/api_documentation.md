# API Документация системы управления библиотекой 
 
## Класс Book 
 
### Конструктор 
```python 
Book(title: str, author: str, isbn: str, publication_year: int) 
``` 
 
### Методы 
- **__str__()** - возвращает строковое представление книги 
- **toggle_availability()** - изменяет статус доступности 
- **get_info()** - возвращает информацию о книге в виде словаря 
 
## Класс Library 
 
### Основные методы 
- **add_book(book: Book)** - добавляет книгу в библиотеку 
- **borrow_book(user_id: int, isbn: str)** - выдает книгу пользователю 
- **return_book(user_id: int, isbn: str)** - принимает возврат книги 
- **find_book_by_title(title: str)** - поиск книг по названию 
- **get_available_books()** - возвращает список доступных книг 
