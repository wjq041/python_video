# coding :  utf-8

"""
@Version : python 3.11
@author:
@contact:
@site:
@IDE: Pycharm
@time:

"""

user_name = '张大仙'
user_gender = 'female'
user_team = 'XYG'
user_dan = '荣耀王者'

# def get_user_info(hero_obj):
#     print(f'玩家属性：名字：{user_name}性别{user_gender}'
#           f'战队：{user_team}段位{user_dan}')
#
# def set_user_name():
#     global user_name
#     user_name='月下无限仙'


# hero_obj = {
#     'hero_work': '射手',
#     'hero_name': '鲁班七号',
#     'hero_speed': 450,
#     'hero_hp': 3000,
#     'hero_atk': 100,
#     'get_hero_info': get_hero_info,
#     'set_hero_speed': set_hero_speed
# }
#
# hero1_obj = {
#     'hero_work': '射手',
#     'hero_name': '后裔',
#     'hero_speed': 460,
#     'hero_hp': 3000,
#     'hero_atk': 110,
#     'get_hero_info': get_hero_info,
#     'set_hero_speed': set_hero_speed
# }


hero_name = '鲁班七号'
hero_speed = 450
hero_hp = 3000
hero_atk = 100


class Hero:
    hero_work = '射手'
    count = 0

    def __init__(self, name, speed, hp, atk):
        self.name = name
        self.speed = speed
        self.hp = hp
        self.atk = atk
        self.equipment = []
        Hero.count += 1

    def get_hero_info(self):
        print(f'英雄属性：名字：{self.name} 移速:{self.speed} '
              f'生命值:{self.hp} 攻击力:{self.atk}')

    def set_hero_speed(self, speed_plus):
        self.speed += speed_plus

    def buy_equipment(self, e_name):
        self.equipment.append(e_name)

    print("xxx")


hero1_obj = Hero('鲁班七号', 450, 3000, 100)
hero2_obj = Hero('虞姬', 470, 3100, 110)
hero3_obj = Hero('后裔', 460, 3200, 120)
hero3_obj.hero_work = '法师'  # 当实例化3里面没有这个定义，就在里面添加一个，不会改变类里面的值
hero1_obj.buy_equipment('反甲')
print(hero1_obj.equipment)


# hero1_obj.get_hero_info()
# hero1_obj.set_hero_speed(20)

# Hero.get_hero_info(hero1_obj)
# Hero.get_hero_info(hero2_obj)
# Hero.get_hero_info(hero3_obj)
#
# Hero.set_hero_speed(hero1_obj, 60)
# Hero.set_hero_speed(hero2_obj, 20)
# Hero.set_hero_speed(hero3_obj, 100)
#
# Hero.get_hero_info(hero1_obj)
# Hero.get_hero_info(hero2_obj)
# Hero.get_hero_info(hero3_obj)
