"""
Теперь потренируемся удалять атрибуты в классе.
Для этого вам необходимо из класса Book удалить три атрибута:

pages
writer
rating
Удаление выполните с помощью оператора del и функции delattr

В этом задании ничего выводить на экран не требуется
"""


# Дано по заданию.
class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    rating = 8.7
    genre = 'dystopian'


# Мое решение
del (Book.pages)
[delattr(Book, attr) for attr in ('writer', 'rating')]
