class User: 
    """Класс, представляющий пользователя библиотеки""" 
 
    def __init__(self, user_id: int, name: str, email: str): 
        Инициализация пользователя 
 
        Args: 
            user_id: Уникальный идентификатор пользователя 
            name: Имя пользователя 
            email: Email пользователя 
        self.user_id = user_id 
        self.name = name 
        self.email = email 
        self.borrowed_books = []  # Список ISBN взятых книг 
 
    def __str__(self) -
        """Строковое представление пользователя""" 
        return f"Пользователь: {self.name} (ID: {self.user_id})" 
 
    def borrow_book(self, isbn: str) -
        Добавление книги в список взятых 
 
        Args: 
            isbn: ISBN книги 
 
        Returns: 
            bool: Успешность операции 
        if isbn not in self.borrowed_books: 
            self.borrowed_books.append(isbn) 
            return True 
        return False 
 
    def return_book(self, isbn: str) -
        Возврат книги 
 
        Args: 
            isbn: ISBN книги 
 
        Returns: 
            bool: Успешность операции 
        if isbn in self.borrowed_books: 
            self.borrowed_books.remove(isbn) 
            return True 
        return False 
 
    def get_borrowed_books(self) -
        """Получение списка взятых книг""" 
        return self.borrowed_books.copy() 
 
    def get_info(self) -
        """Получение информации о пользователе""" 
        return { 
            'user_id': self.user_id, 
            'name': self.name, 
            'email': self.email, 
            'borrowed_books_count': len(self.borrowed_books) 
        } 
