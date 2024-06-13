"""
Перед нами все тот же класс Book, 
но теперь ваша задача получить доступ 
к атрибутам writer и pages при помощи функции getattr
Сначала выведите атрибут writer, затем на новой строке pages
"""

# Дано по заданию.
class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

# Мое решение
[print(getattr(Book, attr)) for attr in ('writer', 'name')]