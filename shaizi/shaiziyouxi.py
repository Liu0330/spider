# -*- coding: utf-8 -*-
# @Time    : 2019/07/14 19:47
# @Author  : Liu
# @File    : exe.py

import random
import time

def enter_stake(current_money):
    '''输入小于结余的赌资及翻倍率,未考虑输入type错误的情况'''
    stake = int(input('How much you wanna bet?(such as 1000):'))
    rate = int(input("What multiplier do you want?你想翻几倍？(such as 2):"))
    small_compare = current_money < stake * rate
    while small_compare == True:
        stake = int(input('You has not so much money ${}!How much you wanna bet?(such as 1000):'.format(stake * rate)))
        rate = int(input("What multiplier do you want?你想翻几倍？(such as 2):"))
        small_compare = current_money < stake * rate
    return stake,rate

def roll_dice(times = 3):
    '''摇骰子'''
    print('<<<<<<<<<< Roll The Dice! >>>>>>>>>>')
    points_list = []
    while times > 0:
        number = random.randrange(1,7)
        points_list.append(number)
        times -= 1
    return points_list

def roll_result(total):
    '''判断是大是小'''
    is_big = 11 <= total <= 18
    is_small = 3 <= total <= 10
    if is_small:
        return 'Small'
    elif is_big:
        return 'Big'

def settlement(boo,points_list,current_money,stake = 1000,rate = 1):
    '''结余'''
    increase = stake * rate
    if boo:
        current_money += increase
        print('The points are ' + str(points_list) + ' .You win!')
        print('You gained $' + str(increase) + '.You have $' + str(current_money) + ' now.' )
    else:
        current_money -= increase
        print('The points are ' + str(points_list) + ' .You lose!')
        print('You lost $' + str(increase) + '.You have $' + str(current_money) + ' now.' )
    return current_money

def sleep_second(seconds=1):
    '''休眠'''
    time.sleep(seconds)


# 开始游戏
def start_game():
    '''开始猜大小的游戏'''
    current_money = 1000
    print('You have ${} now.'.format(current_money))
    sleep_second()
    while current_money > 0:
        print('<<<<<<<<<<<<<<<<<<<< Game Starts! >>>>>>>>>>>>>>>>>>>>')
        your_choice = input('Big or Small: ')
        choices = ['Big','Small']
        if your_choice in choices:
            stake,rate = enter_stake(current_money)
            points_list = roll_dice()
            total = sum(points_list)
            actual_result = roll_result(total)
            boo = your_choice == actual_result
            current_money = settlement(boo,points_list,current_money,stake,rate)
        else:
           print('Invalid input!')
    else:
        sleep_second()
        print('Game Over!')
        sleep_second(2)

if __name__ == '__main__':
    start_game()