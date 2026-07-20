import  sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from typing import cast

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.setting = Setting()

        #创建窗口
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))

        pygame.display.set_caption("Alien Invasion")

        # 禁用输入法
        import ctypes
        hwnd = pygame.display.get_wm_info().get('window')
        if hwnd:
            self.imm32 = ctypes.WinDLL('imm32')
            self.default_ime_context = self.imm32.ImmAssociateContext(hwnd, None)
            self.hwnd = hwnd

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监听键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            #退出程序
            if event.type == pygame.QUIT:
                sys.exit()
            #发射子弹
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            #飞船移动
        keys = pygame.key.get_pressed()
        self.ship.moving_right = keys[pygame.K_d]
        self.ship.moving_left = keys[pygame.K_a]
        self.ship.moving_up = keys[pygame.K_w]
        self.ship.moving_down = keys[pygame.K_s]


    def _check_events_keydown(self,event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    # def _check_events_keydown(self,event):

    def _fire_bullet(self):
        """创建一颗子弹并加入编组"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)  # type: ignore



    def _update_screen(self):
        # 每次循环都重绘屏幕
        self.screen.fill(self.setting.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  # type: ignore
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def enable_ime(self):
        """临时开启输入法"""
        if hasattr(self, 'hwnd') and hasattr(self, 'default_ime_context'):
            # 把之前备份的输入法状态重新绑定给窗口
            self.imm32.ImmAssociateContext(self.hwnd, self.default_ime_context)

    def disable_ime(self):
        """重新关闭输入法"""
        if hasattr(self, 'hwnd'):
            # 再次绑定为 None，打字框就消失了
            self.imm32.ImmAssociateContext(self.hwnd, None)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()