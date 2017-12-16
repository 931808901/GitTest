import pygame
from pygame.sprite import Sprite

# 继承于精灵类
class Hero(Sprite):

    # 创建英雄对象
    def __init__(self,winWidth,winHeight):
        super().__init__()
        self.winWidth = winWidth
        self.winHeight = winHeight

        # 加载英雄图片
        self.mSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
        self.mSurface2 = pygame.image.load("./images/me2.png").convert_alpha()
        self.rect = self.mSurface1.get_rect()
        self.speed = 10

        self.rect.left = self.winWidth // 2 - self.rect.width // 2
        self.rect.top = self.winHeight - 50 - self.rect.height

        # 从mSurface1生成非透明区域遮罩，用于做碰撞检测
        self.mask = pygame.mask.from_surface(self.mSurface1)

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.right < self.winWidth:
            self.rect.left += self.speed

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.bottom < self.winHeight:
            self.rect.bottom += self.speed

    def move(self,dx,dy):
        self.rect.left += dx
        self.rect.top += dy
