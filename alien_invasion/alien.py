import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        #加载图像并设置rect属性
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        #每个外形人都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def update(self):
        """向右移动"""
        self.x += self.setting.alien_speed*self.setting.alien_direction
        self.rect.x = self.x


    def check_edges(self):
        """如果在边缘就返回TRUE"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)