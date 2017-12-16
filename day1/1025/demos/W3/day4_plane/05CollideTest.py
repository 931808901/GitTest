#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import pygame
import sys

from demos.W3.day4_plane.Constants import WIN_WIDTH, WIN_HEIGHT
from demos.W3.day4_plane.Hero import Hero

if __name__ == "__main__":
    # 全局初始化
    pygame.init()
    pygame.mixer.init()

    # 加载背景音乐
    pygame.mixer.music.load("./sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # 加载音效并设置音量
    bombSound = pygame.mixer.Sound("./sound/enemy1_down.wav")
    bombSound.set_volume(0.5)

    # 窗口（尺寸）和标题
    winSurface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("科学打飞机")

    # 加载背景图片
    bgSurface = pygame.image.load("./images/background.png").convert()
    heroSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
    heroSurface2 = pygame.image.load("./images/me2.png").convert_alpha()

    # 加载字体文件并创建文本表面
    textFont = pygame.font.Font("./font/font.ttf", 30)
    textSurface = textFont.render("SCORE:00000", True, (0, 0, 255))

    # 创建全局时钟
    clock = pygame.time.Clock()

    # 创建英雄角色
    hero = Hero((heroSurface1, heroSurface2))

    # 创建敌军
    wangchao = Hero((heroSurface1, heroSurface2))
    mahan = Hero((heroSurface1, heroSurface2))
    wangchao.move(-60,-150)
    mahan.move(60,-150)
    myGroup = pygame.sprite.Group()
    myGroup.add(wangchao, mahan)

    # 记录当前的帧序号
    count = 0

    # 消息循环（一秒循环60次）
    # 不断重绘，不断处理用户交互
    while True:
        # 绘制背景（将图片转为Surface，绘制Surface）
        winSurface.blit(bgSurface, (0, 0))

        # 绘制英雄
        if count % 5 == 0:
            hs = hero.surfaces[0]
        else:
            hs = hero.surfaces[1]
        # 将英雄绘制在【其rect的左上角】位置
        winSurface.blit(hs, (hero.rect.left, hero.rect.top))
        winSurface.blit(wangchao.surfaces[0], (wangchao.rect.left, wangchao.rect.top))
        winSurface.blit(mahan.surfaces[0], (mahan.rect.left, mahan.rect.top))

        # 绘制文字
        winSurface.blit(textSurface, (10, 10))

        # 刷新界面
        pygame.display.flip()

        # 处理事件（获取当前帧的所有用户事件，遍历处理之）
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 处理鼠标事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # print("您老人家DOWN了鼠标在：", event.pos)
                # 如果点击了英雄的矩形，就令其大吼一声“别摸我”
                if hero.rect.collidepoint(event.pos) == True:
                    print("别摸我")
            elif event.type == pygame.MOUSEMOTION:
                # print("您老人家乱动鼠标在：",event.pos)
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                print("您老人家UP了鼠标在：", event.pos)

            # 处理键盘事件（状态改变才会触发）
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_SPACE:
                    print("发射导弹")
                    bombSound.play()

        # 处理键盘状态事件
        boolsTuple = pygame.key.get_pressed()
        # print(boolsTuple)
        if boolsTuple[pygame.K_UP] == True:
            # print("向他娘的前飞")
            hero.moveUp()
        if boolsTuple[pygame.K_DOWN] == True:
            hero.moveDown()
        if boolsTuple[pygame.K_LEFT] == True:
            hero.moveLeft()
        if boolsTuple[pygame.K_RIGHT] == True:
            hero.moveRight()

        # 检测英雄有没有撞到【僚机】
        hitList = pygame.sprite.spritecollide(hero, myGroup, False, collided=pygame.sprite.collide_mask)
        if len(hitList) > 0:
            print(len(hitList))

        # 设置时钟和帧率（当前帧停留1/60秒）
        clock.tick(60)
        count += 1

        pass

    print("main over")
