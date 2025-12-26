# a = '{0:*^20}'.format('开始')
# print(a)
#
# a = {'李白': '刺客', '孙尚香': '刺客'}
import time

# 装饰器
# #开放封闭原则
# 开放：对扩展功能开放，在源代码不变的情况下，增加其他功能
# 封闭：对修改源代码封闭

# import time


# fun 1:
# def inside(group, s):
#     start = time.time()
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#     end = time.time()
#     print(end-start)
#
#
# inside('红色', 5)

# fun 2
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# start = time.time()
# inside('红色', 5)
# end = time.time()
# print(end - start)


# fun3
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
# def wrapper ():
#     start = time.time()
#     inside('红色', 5)
#     end = time.time()
#     print(end - start)
#
# wrapper()

# fun4
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# def wrapper(*args, **kwargs):
#     start = time.time()
#     inside(*args, **kwargs)
#     end = time.time()
#     print(end - start)
#
#
# wrapper('蓝色', 3, '炮车')


# fun5
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# def outer(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         inside(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#
#     return wrapper
#
#
# inside = outer(inside)
# inside('蓝色', s=3, z='跑车')


# fun6
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# def recharge(num):
#     for i in range(num, 100):
#         time.sleep(0.05)
#         print(f'\r当前电量：{"∎" * i} {i}%', end='')
#     print('电量已经充满！')
#
#
# def outer(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#
#     return wrapper
#
#
# recharge = outer(recharge)
# recharge(20)


# fun 7
# def counter_time(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         response = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return response
#
#     return wrapper
#
#
# @counter_time  # inside = outer(insider)
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# @counter_time  # recharge = outer(recharge)
# def recharge(num):
#     for i in range(num, 100):
#         time.sleep(0.05)
#         print(f'\r当前电量：{"∎" * i} {i}%', end='')
#     print('电量已经充满！')
#
#
# inside('蓝色', s=3, z='跑车')
# recharge(50)

# import time
# from functools import wraps
#
#
# def auth(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         name = input('input your account>>>').strip()
#         pwd = input('input your password').strip()
#         if name == 'jack' and pwd == '123':
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('wrong username or password')
#
#     # wrapper.__name__ = func.__name__
#     # wrapper.__doc__ = func.__doc__
#     return wrapper
#
#
# @auth
# def home():
#     '''This is main page'''
#     time.sleep(2)
#     print('Welcome')
#
#
# # home()
#
# print(home)
# print(home.__doc__)
# print(home.__name__)

# import time
#
#
# def pa_outer(x):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return outer
#
#
# outer = g_outer('Now')
#
#
# @g_outer('now')   #@outer home = outer(home)  home = wrapper
# def home():
#     time.sleep(2)
#     print('Welcome')
#
# @outer
# def gettime():
#     print(time.localtime())
#
# home()
# gettime()


# l = ['a', 'b', 'c']
# num = 0
# while num < len(l):
#     print(l[num])
#     num += 1


# with open('file.txt', mode='rt', encoding='utf-8') as f:
#     size = 0
#     # 1
#     for line in f:
#         size += len(line)
#     print(size)
#
#     # 2
#     size = sum([len(line) for line in f])
#
#     # 3
#     size = sum(len(line) for line in f)


#
# s = 'abcd'
# l = list(s)
# def permutation(l, level):
#     if level == len(l):
#         print(l)
#     for i in range(level, len(l)):
#         l[level], l[i] = l[i], l[level]
#         permutation(l, level + 1)
#         l[level], l[i] = l[i], l[level]
# permutation(l, 0)
#

# 递归二分法查找元素
#
# l = [-6, -10, -7, -3, -2, -1, 0, 2, 4, 6, 7, 8, 9, 11, 13]
# l_after = sorted(l)
# result = 8
# def dichotomy(my_list, value):
#     if len(my_list) == 0:
#         print('Value not in the list')
#
#     if my_list[int(len(my_list) / 2)] > value:
#         my_list = my_list[:int((len(my_list) - 1) / 2)]
#         dichotomy(my_list,value)
#     elif my_list[int(len(my_list) / 2)] < value:
#         my_list = my_list[int(len(my_list) / 2):]
#         dichotomy(my_list,value)
#     else:
#         print(f'Find the value {value}')
#
#
# dichotomy(l_after, result)


# 匿名函数

# def func(x,y):
#     return x+y
#
# res = (lambda x, y :x+y)(1,3)
# print(res)
# import copy
#
# # l = [1,2,3,4,5,6,7]
# #
# # res = map(lambda name: str(name)+'_item',l)
# #
# # # for i in res:
# # #     print(i)
# # print(res.__next__())
#
#
# def func(name: str, age: int=88) -> int:
#     print(name)
#     print(age)
#     return 10


# print(func.__annotations__)



# if __name__ == '__main__':
#     print('This is new module')
#
# from module import name

#!/usr/bin/python  #only work in Unix, define the interpreter path


# """
# Module description
# """
#
# import time # import module
#
# name = 'xxx'  #define the global variable
#
# class Test: # define class
#     """
#     class description
#     """
#     pass
#
# def func():        #define the function
#     """
#     function description
#     :return:
#     """
#     pass
#
# if __name__ == '__main__':
#     func()





























