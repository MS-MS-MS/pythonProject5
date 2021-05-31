# -*- coding: utf-8 -*-
""" 
@Time    : 2021/5/28 11:06
@Author  : ms
@FileName: game_functions.py.py
@SoftWare: PyCharm
"""
import  sys
import pygame

def check_events():
    """相应鼠标的事件"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    """更新屏幕的图像，并换到新的屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
