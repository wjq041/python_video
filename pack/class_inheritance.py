# coding :  utf-8

"""
@Version : python 3.11
@author:
@contact:
@site:
@IDE: Pycharm
@time:

"""


# 在python2 里面，有新式类和经典类的区分
# 新式类： 继承了object 类的子类，以及继承了这个类的子子孙孙类
# python3 里面都是新式类
# 继承的特性是遗传
# 多继承  只有在python里面才有
# 优点： 一个子类可以同时遗传多个父类的属性
# 缺点
# 让代码的可读性变差
# 多继承需要使用Mixins 机制
#
# class Human:
#     star = 'earth'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Chinese(Human):
#     # star = 'earth'
#     nation = 'China'
#
#     def __init__(self, name, age, gender, balance):
#         Human.__init__(self, name, age, gender)
#         self.balance = balance
#
#     def speak_Chinese(self):
#         print(f'{self.name}再说普通话')
#
#
# class American(Human):
#     # star = 'earth'
#     nation = 'America'
#
#     #
#     # def __int__(self, name, age, gender):
#     #     self.name = name
#     #     self.age = age
#     #     self.gender = gender
#
#     def speak_english(self):
#         print(f'{self.name}在说英语')
#
#
# dy_obj = Chinese('董永', 18, '男', 10000)
#
# print(dy_obj.nation)
# print(dy_obj.__dict__)
# print(dy_obj.star)
# dy_obj.speak_Chinese()
#
# iron_man_obj = American('iron_man', 19, 'male')
# print(iron_man_obj.nation)
# print(iron_man_obj.__dict__)
# print(iron_man_obj.star)
# iron_man_obj.speak_english()


class Test1:
    def f1(self):
        print('Test1.f1')

    def f2(self):
        print('Test1.f2')
        self.f1()


class Test2(Test1):
    def f1(self):
        print('Test2.f1')


obj = Test2()
obj.f2()
print(Test1.mro())
print(Test2.mro())
