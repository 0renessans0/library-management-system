# Инструкция по установке и запуску 
 
## Требования 
- Python 3.8 или выше 
- Git (для клонирования репозитория) 
 
## Установка 
 
1. Клонируйте репозиторий: 
```bash 
git clone https://github.com/0renessans0/library-management-system.git 
cd library-management-system 
``` 
 
2. (Опционально) Установите зависимости для тестирования: 
```bash 
pip install pytest 
``` 
 
## Запуск 
 
### Основное приложение: 
```bash 
python src/main.py 
``` 
 
### Тестирование: 
```bash 
python -m pytest tests/ -v 
``` 
