import pygame
from pygame.locals import *
import random

# 初始化
pygame.init()
# 定义屏幕宽，高
WIDTH = 480
HEIGHT = 600



# 定义飞机类
class Plane:
    def __init__(self):
        # 加载飞机图片
        self.image = pygame.image.load('C:/item/10-太空狙击（三）-工程包/img/img_plane.png')
        # 设置飞机初始位置
        self.rect = self.image.get_rect()
        # 设置飞机长方形中心的X的值
        self.rect.centerx = WIDTH / 2
        # 设置飞机长方形底边的值
        self.rect.bottom = HEIGHT - 10

    def update(self):
        # 初始化速度为 0
        self.speedx = 0
        # 获取按键状态
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -8
        if keys[pygame.K_RIGHT]:
            self.speedx = 8
        # 根据速度改变飞机位置
        self.rect.centerx += self.speedx
        # 飞机左右移动限制
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Bullet:
    def __init__(self, x, y):
        # 加载子弹图片
        self.image = pygame.image.load('C:/item/10-太空狙击（三）-工程包/img/img_bullet.png')
        # 设置子弹初始位置
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        # 设置子弹移动速度
        self.speedy = -10

    def update(self):
        # 根据速度改变子弹位置
        self.rect.y += self.speedy
        # 如果子弹移出屏幕则删除
        if self.rect.bottom < 0:
            self.kill()

# 定义陨石类
class Meteorite:
    def __init__(self):
        # 加载陨石图片
        self.image_orig = pygame.image.load('C:/item/10-太空狙击（三）-工程包/img/img_meteorite.png')
        self.image = self.image_orig.copy()
        # 设置陨石初始位置
        self.rect = self.image.get_rect()
        # 设置陨石X的初始位置为0到屏幕X大小减角色X大小的随机数
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        # 设置陨石Y的初始位置为负角色Y大小，即在屏幕上方看不见的地方
        self.rect.y = -self.rect.height
        # 设置陨石的旋转角度和移动速度是随机的，X的移动随机数取值范围为-3~3，Y的移动随机数取值范围为1~8
        self.rot = 0
        self.speedx = random.randrange(-3, 4)
        self.speedy = random.randrange(1, 9)

    def update(self):
        # 根据速度改变陨石位置和旋转角度，更新陨石图片旋转状态。
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rot = (self.rot + 5) % 360
        self.image = pygame.transform.rotate(self.image_orig, self.rot)
        # 如果陨石移出屏幕则删除
        if self.rect.top > HEIGHT:
            self.kill()

# 控制帧速率为60，即每秒执行60次循环。
clock = pygame.time.Clock()
FPS = 60

planes = []
plane = Plane()
planes.append(plane)

meteorites = pygame.sprite.Group()

running = True
while running:
    clock.tick(FPS)
    for plane in planes:
        plane.update()
    # 检测子弹和陨石之间的碰撞
    hits = pygame.sprite.groupcollide(meteorites, bullets, True, True)
    # 对于每次碰撞，创建一个新的陨石对象并添加到列表中
    for hit in hits:
        meteorite = Meteorite()
        meteorites.add(meteorite)
    for meteorite in meteorites:
        meteorite.update()
    if random.random() < 0.02:
        meteorite = Meteorite()
        meteorites.append(meteorite)
    screen.blit(bg, (0, 0))
    for plane in planes:
        screen.blit(plane.image, plane.rect)
    for meteorite in meteorites:
        screen.blit(meteorite.image, meteorite.rect)
    pygame.display.flip()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False 
        elif event.key == pygame.K_SPACE:
            # 按下空格键发射子弹
            bullet = Bullet(plane.rect.centerx, plane.rect.top)
            bullets.add(bullet)

pygame.quit()
