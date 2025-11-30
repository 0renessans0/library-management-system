class Book: 
    """Класс, представляющий книгу в библиотечной системе""" 
 
    def __init__(self, title: str, author: str, isbn: str, publication_year: int): 
        Инициализация книги 
 
        Args: 
            title: Название книги 
            author: Автор книги 
            isbn: ISBN номер 
            publication_year: Год публикации 
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        self.publication_year = publication_year 
        self.is_available = True 
 
    def __str__(self) -
        """Строковое представление книги""" 
        status = "доступна" if self.is_available else "выдана" 
        return f"'{self.title}' - {self.author} ({self.publication_year}) - {status}" 
 
    def toggle_availability(self) -
        """Изменение статуса доступности книги""" 
        self.is_available = not self.is_available 
 
    def get_info(self) -
        """Получение информации о книге в виде словаря""" 
        return { 
            'title': self.title, 
            'author': self.author, 
            'isbn': self.isbn, 
            'publication_year': self.publication_year, 
            'is_available': self.is_available 
        } 
