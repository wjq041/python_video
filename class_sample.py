# coding :  utf-8

"""
@Version : python 3.11
@author:
@contact:
@site:
@IDE: Pycharm
@time:

"""


class Test:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name

    @property  # age = property(age)
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if type(new_age) is not int:
            print('你个傻子')
            return

        if not 0 < new_age < 150:
            print('你个傻子，年龄应该在0到150之间')
            return
        self.__age = new_age

    @age.deleter
    def age(self):
        del self.__age

obj = Test('xxx', 18)
obj.age=20
print(obj.age)



