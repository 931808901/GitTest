#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import pygame
from pygame.sprite import Sprite

from demos.W3.day4_plane.Constants import *


class Hero(Sprite):
    def __init__(self,surfaces):
        super(Hero, self).__init__()
        self.surfaces = surfaces

        self.rect = self.surfaces[0].get_rect()

        # 初始化英雄位置
        self.rect.left = WIN_WIDTH // 2 - self.rect.width // 2
        self.rect.top = WIN_HEIGHT - BOTTOM_OFFSET - self.rect.height

        # 创建碰撞检测遮罩
        self.mask = pygame.mask.from_surface(self.surfaces[0])

        self.speed = 10#飞行速度为10像素/帧

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.right < WIN_WIDTH:
            self.rect.right += self.speed

    def moveDown(self):
        if self.rect.bottom < WIN_HEIGHT:
            self.rect.top += self.speed

    def moveUp(self):
        # print("亲爱的你慢慢飞")
        if self.rect.top > 0:
            self.rect.top -= self.speed

    def move(self,dx,dy):
        self.rect.left += dx
        self.rect.top += dy

class Bullet(Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surface = pygame.image.load("./images/bullet1.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.speed = 20
        self.isAlive = False

    def move(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.isAlive = False

    pass

if __name__ == "__main__":
    print("main over")