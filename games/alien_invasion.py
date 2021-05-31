# -*- coding: utf-8 -*-
""" 
@Time    : 2021/5/27 16:37
@Author  : MaSai
@FileName: alien_invasion.py
@SoftWare: PyCharm
"""
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    # #游戏初始化 创建一个屏幕对象
    pygame.init()
    ai_seetings=Settings()
    # 设置屏幕的大小
    screen=pygame.display.set_mode((ai_seetings.screen_with,ai_seetings.screen_height))
    # 设置游戏的标题
    pygame.display.set_caption("Alien Invasion")
    # 创建一个飞船
    ship =Ship(screen)
    #开始 游戏循环
    while True:
        #监听键盘和鼠标
        gf.check_events()
        # 设置屏幕颜色
        gf.update_screen(ai_seetings,screen,ship)
run_game()


