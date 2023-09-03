'''太空狙击（四）'''
import random
import time
import pygame
from pygame.locals import *
# 初始化
pygame.init()
font_name = pygame.font.match_font("黑体")
font = pygame.font.Font(None, 36)
score = 0
health = 100

# 定义飞机类
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        # 完成角色的初始化
        pygame.sprite.Sprite.__init__(self)
        # 加载飞机图片
        self.image = pygame.image.load('C:/item/11-太空狙击（四）-工程包/11-太空狙击（四）-工程包/img/img_plane.png')
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
        self.rect.left += self.speedx
        # 飞机左右移动限制
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    # 添加射击功能
    def shoot(self):
        # 生成子弹对象
        bullet = Bullet(self.rect.centerx, self.rect.top)
        # 将子弹加入角色组
        all_sprites.add(bullet)
        all_bullets.add(bullet)
        


# 定义陨石类
class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        # 初始化
        pygame.sprite.Sprite.__init__(self)
        # 定义陨石的图形
        self.image = pygame.image.load('C:/item/11-太空狙击（四）-工程包/11-太空狙击（四）-工程包/img/img_meteorite.png')
        # 获取陨石的长方形
        self.rect = self.image.get_rect()
        # 设置出现的位置
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        # 设定运行速度
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # 陨石移出屏幕后再次回到屏幕上方随机位置
        if self.rect.top > HEIGHT + 10 or self.rect.left < -30 or self.rect.right > WIDTH + 30:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)


# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:/item/11-太空狙击（四）-工程包/11-太空狙击（四）-工程包/img/img_bullet.png')
        self.rect = self.image.get_rect()
        # 设置出现的位置
        self.rect.y = y
        self.rect.centerx = x
        # 设置子弹由下往上飞的速度
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # 子弹移出屏幕后将此子弹对象删除
        if self.rect.bottom < 0:
            self.kill()

def draw_health_bar(surface, x, y, health, width, height):
    fill = (health / 100) * width
    outline_rect = pygame.Rect(x, y, width, height)
    fill_rect = pygame.Rect(x, y, fill, height)
    pygame.draw.rect(surface, (255, 0, 0), fill_rect)
    pygame.draw.rect(surface, (255, 255, 255), outline_rect, 2)

# 定义屏幕宽，高
WIDTH = 480
HEIGHT = 600

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 加载背景图片
bg = pygame.image.load('C:/item/11-太空狙击（四）-工程包/11-太空狙击（四）-工程包/img/img_bg.jpg')

# 定义飞机
plane = Plane()

# 创建角色组并将飞机添加到组中
all_sprites = pygame.sprite.Group()
all_sprites.add(plane)

# 定义陨石组
all_meteorite = pygame.sprite.Group()
# 创建子弹角色组
all_bullets = pygame.sprite.Group()


# 定义生成陨石
for i in range(8):
    # time.sleep(random.random(0.1,5))
    met = Meteorite()
    all_sprites.add(met)
    all_meteorite.add(met)

# 控制帧速率
clock = pygame.time.Clock()
# 帧速率为60，即每秒执行60次循环
FPS = 60

running = True
while running:
    # 控制帧速率也就是每秒内循环执行的次数
    clock.tick(FPS)
    # 绘制背景
    screen.blit(bg, (0, 0))
    # 通过角色组调用所有角色的update方法
    all_sprites.update()
    # 将所有角色绘制到屏幕中
    all_sprites.draw(screen)
    # 计算得分文本
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    # 绘制血条
    bar_width = 200  # 调整血条的长度
    bar_height = score_text.get_height()
    health_bar_x = 20 + score_text.get_width() + 10
    health_bar_y = 10
    draw_health_bar(screen, health_bar_x, health_bar_y, health, bar_width, bar_height)
    # 判断飞机与陨石的碰撞
    hits1 = pygame.sprite.spritecollide(plane, all_meteorite, True)
    if hits1:
        # 减少生命值
        health -= 20  # 或者根据需要减少的量来设定
        # 判断血量是否为0，若为0则结束游戏循环
        if health <= 0:
            running = False
    # 判断子弹与陨石的碰撞
    hits2 = pygame.sprite.groupcollide(all_bullets, all_meteorite, True, True)
    # 利用字典遍历,补充陨石
    for hit in hits2:
        score += 5
        meteorite = Meteorite()
        all_sprites.add(meteorite)
        all_meteorite.add(meteorite)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 点击叉号结束游戏
            running = False
        elif event.type == pygame.KEYDOWN:
            # 添加射击按键检测
            if event.key == pygame.K_SPACE:
                plane.shoot()
            if event.key == pygame.K_ESCAPE:
                # 按下ESC键结束游戏
                running = False
    # 重绘界面，相当于刷新
    pygame.display.flip()

# 彻底退出
pygame.quit()
