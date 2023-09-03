'''太空狙击（二）'''
import pygame
from pygame.locals import *
# 初始化
class Plane:
    def __init__(self):
        self.image = pygame.image.load("C:/item/09-太空狙击（二）-工程包/img/img_plane.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100        
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10
    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            print("pygame.K_RIGHT",pygame.K_RIGHT)
            self.speedx = 8
        if keys[pygame.K_LEFT]:
            print("pygame.K_LEFT",pygame.K_LEFT)
            self.speedx = -8
        self.rect.left += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
pygame.init()

# 定义屏幕宽，高
WIDTH = 480
HEIGHT = 600

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("C:/item/09-太空狙击（二）-工程包/img/img_bg.jpg")
plane = Plane()
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    clock.tick(FPS)
    plane.update()
    screen.blit(bg,(0,0))
    screen.blit(plane.image,plane.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 点击叉号结束游戏
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # 按下ESC键结束游戏
                running = False 

# 彻底退出
pygame.quit()
