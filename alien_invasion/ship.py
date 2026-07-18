import pygame
import setting

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting

        #加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('images/airship.png').convert_alpha()
        self.rect = self.image.get_rect()

        #飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        #浮点存储初始坐标
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x
        if self.moving_up and self.rect.y > 0:
            self.y -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.setting.ship_speed
        self.rect.y = self.y

