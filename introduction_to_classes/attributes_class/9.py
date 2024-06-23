"""
В вашем распоряжении класс Person, у которого имеется 7 атрибутов.
Программа будет принимать на вход произвольное количество слов в одну строку, 
разделенных пробелом. Ваша задача проверить, является ли каждое из введенных слов 
названием атрибута. Регистр слов значения не имеет.Нужно вывести в каждой отдельной 
строке введенные слова по порядку и напротив через дефис указать, нашлось свойство 
с таким именем или нет (вывести YES или NO)
"""


# Дано по заданию.
class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


# Мое решение
def print_bool_answer(line: str) -> str:
    return '\n'.join(['-'.join([word, ("NO", "YES")[hasattr(Person, word)]]) for word in input().split()])


# test1 =  
# test2 = 
# test3 = 
assert print_bool_answer('age date address') == 'age-YES\ndate-NO\naddress-YES'