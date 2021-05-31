# -*- coding: utf-8 -*-
""" 
@Time    : 2021/5/28 10:25
@Author  : ms
@FileName: ship.py
@SoftWare: PyCharm
"""
import pygame

class Ship ():
    def __init__(self,screen):
        """初始化f飞船比并设置位置"""
        self.screen=screen

        # 加载飞船图像并获取其外接矩形
        date=r"C:\Users\Administrator\PycharmProjects\pythonProject5\images\ship.bmp"
        self.image=pygame.image.load(date)
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        # 将每个新飞船的位置 设置到屏幕的底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image,self.rect)