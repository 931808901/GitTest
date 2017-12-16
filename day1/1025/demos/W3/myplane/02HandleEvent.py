import pygame
import sys

# 全局初始化
pygame.init()

# 设置窗口大小和标题
resolution = width, height = 480, 700
windowSurface = pygame.display.set_mode(resolution)  # 设置分辨率并得到全局的绘图表面
pygame.display.set_caption("飞机大战")

# 加载背景图
bgSurface = pygame.image.load("./images/background.png").convert()

# 创建时钟对象
clock = pygame.time.Clock()

if __name__ == '__main__':

    # 开启消息循环
    while True:

        # 处理用户输入
        for event in pygame.event.get():

            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 感应和处理鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("MOUSEBUTTONDOWN @ ", event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                print("MOUSEBUTTONUP @ ", event.pos)
            if event.type == pygame.MOUSEMOTION:
                # print("MOUSEMOTION @ ", event.pos)
                pass

            # 处理键盘事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("开炮!")
                if event.key == pygame.K_LEFT:
                    print("左1")

        # 检测当前按下的按钮有哪些
        bools = pygame.key.get_pressed()
        # print(type(bools),bools)#<class 'tuple'>
        if bools[pygame.K_UP] == 1:
            print("上")
        if bools[pygame.K_DOWN] == 1:
            print("下")
        if bools[pygame.K_LEFT] == 1:
            print("左2")
        if bools[pygame.K_RIGHT] == 1:
            print("右")

        # 绘制背景
        windowSurface.blit(bgSurface, (0, 0))

        # 刷新界面
        pygame.display.flip()

        # 时钟停留一帧的时长
        clock.tick(60)
        pass
