# API „®Єг¬Ґ­в жЁп бЁбвҐ¬л гЇа ў«Ґ­Ёп ЎЁЎ«Ё®вҐЄ®© 
 
## Љ« бб Book 
 
### Љ®­бвагЄв®а 
```python 
Book(title: str, author: str, isbn: str, publication_year: int) 
``` 
 
### ЊҐв®¤л 
- **__str__()** - ў®§ўа й Ґв бва®Є®ў®Ґ ЇаҐ¤бв ў«Ґ­ЁҐ Є­ЁЈЁ 
- **toggle_availability()** - Ё§¬Ґ­пҐв бв вгб ¤®бвгЇ­®бвЁ 
- **get_info()** - ў®§ўа й Ґв Ё­д®а¬ жЁо ® Є­ЁЈҐ ў ўЁ¤Ґ б«®ў ап 
 
## Љ« бб Library 
 
### Ћб­®ў­лҐ ¬Ґв®¤л 
- **add_book(book: Book)** - ¤®Ў ў«пҐв Є­ЁЈг ў ЎЁЎ«Ё®вҐЄг 
- **borrow_book(user_id: int, isbn: str)** - ўл¤ Ґв Є­ЁЈг Ї®«м§®ў вҐ«о 
- **return_book(user_id: int, isbn: str)** - ЇаЁ­Ё¬ Ґв ў®§ўа в Є­ЁЈЁ 
- **find_book_by_title(title: str)** - Ї®ЁбЄ Є­ЁЈ Ї® ­ §ў ­Ёо 
- **get_available_books()** - ў®§ўа й Ґв бЇЁб®Є ¤®бвгЇ­ле Є­ЁЈ 
