import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射子弹的类"""

    def __init__(self,ai_game):
        """在飞船的当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        #创建子弹再设置位置
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #存储子弹位置
        self.y = float(self.rect.y)


    def update(self):
        """上移子弹"""
        #更新子弹的准确位置
        self.y -= self.setting.bullet_speed
        #更新子弹rect位置
        self.rect.y = self.y


    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)