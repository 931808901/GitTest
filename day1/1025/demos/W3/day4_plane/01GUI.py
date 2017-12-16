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

        # 设置时钟和帧率（当前帧停留1/60秒）
        clock.tick(60)

        pass

    print("main over")