from services.library import Library 
from models.book import Book 
from models.user import User 
 
def initialize_sample_data(library: Library): 
    """Инициализация тестовыми данными""" 
    # Добавление книг 
    books_data = [ 
        ("Преступление и наказание", "Ф.М. Достоевский", "978-123", 1866), 
        ("1984", "Джордж Оруэлл", "978-456", 1949), 
        ("Мастер и Маргарита", "М.А. Булгаков", "978-789", 1967), 
        ("Война и мир", "Л.Н. Толстой", "978-012", 1869), 
        ("Анна Каренина", "Л.Н. Толстой", "978-345", 1877) 
    ] 
 
    for title, author, isbn, year in books_data: 
        book = Book(title, author, isbn, year) 
        library.add_book(book) 
 
    # Регистрация пользователей 
    users_data = [ 
        (1, "Иван Петров", "ivan@example.com"), 
        (2, "Мария Сидорова", "maria@example.com"), 
        (3, "Алексей Иванов", "alex@example.com") 
    ] 
 
    for user_id, name, email in users_data: 
        user = User(user_id, name, email) 
        library.register_user(user) 
 
def display_library_info(library: Library): 
    """Отображение информации о библиотеке""" 
    print("=== СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ ===") 
    print(f"Всего книг: {len(library.books)}") 
    print(f"Зарегистрированных пользователей: {len(library.users)}") 
 
    available_books = library.get_available_books() 
    print(f"\\nДоступные книги ({len(available_books)}):") 
    for book in available_books: 
        print(f"  - {book}") 
 
    print("\\nЗарегистрированные пользователи:") 
    for user in library.users.values(): 
        print(f"  - {user}") 
 
def demonstrate_functionality(library: Library): 
    """Демонстрация функциональности""" 
    print("\\n=== ДЕМОНСТРАЦИЯ ФУНКЦИОНАЛЬНОСТИ ===") 
 
    # Выдача книги 
    print("\\n1. Выдача книги пользователю Иван Петров:") 
    if library.borrow_book(1, "978-123"): 
        print("   Книга 'Преступление и наказание' успешно выдана!") 
    else: 
        print("   Ошибка при выдаче книги") 
 
    # Поиск книг 
    print("\\n2. Поиск книг Толстого:") 
    tolsto_books = library.find_book_by_author("Толстой") 
    for book in tolsto_books: 
        print(f"   - {book}") 
 
    # Просроченные выдачи 
    overdue_loans = library.get_overdue_loans() 
    print(f"\\n3. Просроченных выдач: {len(overdue_loans)}") 
 
def main(): 
    """Основная функция приложения""" 
    library = Library() 
 
    # Инициализация тестовыми данными 
    initialize_sample_data(library) 
 
    # Отображение информации 
    display_library_info(library) 
 
    # Демонстрация функциональности 
    demonstrate_functionality(library) 
 
    print("\\n=== ПРОГРАММА ЗАВЕРШЕНА ===") 
 
if __name__ == "__main__": 
    main() 
