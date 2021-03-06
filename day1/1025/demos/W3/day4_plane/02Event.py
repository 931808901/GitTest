#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import pygame
import sys

if __name__ == "__main__":
    # 全局初始化
    pygame.init()

    # 窗口（尺寸）和标题
    winSurface = pygame.display.set_mode((480,700))
    pygame.display.set_caption("科学打飞机")

    # 加载背景图片
    bgSurface = pygame.image.load("./images/background.png").convert()

    # 创建全局时钟
    clock = pygame.time.Clock()

    # 消息循环（一秒循环60次）
    # 不断重绘，不断处理用户交互
    while True:
        # 绘制背景（将图片转为Surface，绘制Surface）
        winSurface.blit(bgSurface, (0, 0))

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
                print("您老人家DOWN了鼠标在：",event.pos)
            elif event.type == pygame.MOUSEMOTION:
                # print("您老人家乱动鼠标在：",event.pos)
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                print("您老人家UP了鼠标在：",event.pos)

            # 处理键盘事件（状态改变才会触发）
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_SPACE:
                    print("向我开炮")
                if event.key == pygame.K_UP:
                    print("向前飞")

        # 处理键盘状态事件
        boolsTuple = pygame.key.get_pressed()
        # print(boolsTuple)
        if boolsTuple[pygame.K_UP] == True:
            print("向他娘的前飞")

        # 设置时钟和帧率（当前帧停留1/60秒）
        clock.tick(60)

        pass

    print("main over")