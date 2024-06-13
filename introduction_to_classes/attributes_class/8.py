"""
Реализуйте функцию is_obj_has_attr, которая принимает любой объект в качестве первого аргумента и название атрибута в качестве второго
Функция is_obj_has_attr должна возвращать True, если в объекте имеется атрибут с указанным названием, либо вернуть False.
Ваша задача написать только определение функции is_obj_has_attr
"""

def is_obj_has_attr(class_name, attr_class)  -> bool:
    return hasattr(class_name, attr_class)


class Duck:
    weight = 5
    height = 10


assert is_obj_has_attr(Duck, 'weight') == True
assert is_obj_has_attr(Duck, 'name') == False
assert is_obj_has_attr(Duck, 'height') == True


class House:
    color = 'white'
    rooms = 4

assert is_obj_has_attr(House, 'color') == True
assert is_obj_has_attr(House, 'rooms') == True
assert is_obj_has_attr(House, 'room') == False 


class House:
    color = 'white'
    rooms = 4

assert is_obj_has_attr(House, 'age') == False
assert is_obj_has_attr(House, 'kids') == False
assert is_obj_has_attr(House, 'cat') == False
