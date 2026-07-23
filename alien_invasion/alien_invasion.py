import  sys
import pygame
from time import  sleep

from pygame.constants import MOUSEBUTTONDOWN

from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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

        #创建统计信息的示例
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # 禁用输入法
        import ctypes
        hwnd = pygame.display.get_wm_info().get('window')
        if hwnd:
            self.imm32 = ctypes.WinDLL('imm32')
            self.default_ime_context = self.imm32.ImmAssociateContext(hwnd, None)
            self.hwnd = hwnd

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #游戏启动后处于非活动状态
        self.game_active = False

        #创建play按钮
        self.play_button = Button(self,'Play')


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监听键盘和鼠标事件
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)


    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_aliens_bullets_collisions()


    def _check_aliens_bullets_collisions(self):
        """响应子弹和外星人的碰撞"""
        # 检查是否有子弹击中外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score +=self.setting.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()

        if not self.aliens:
            # 删除现有子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()


    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕下边缘"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.setting.screen_height:
                #像飞船被撞到一样处理
                self._ship_hit()
                break


    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，更新所有外星人的位置"""
        self._check_fleet_edge()
        self.aliens.update()

        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #检查是否有外星人到达屏幕下边
        self._check_aliens_bottom()


    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        if self.stats.ships_left > 0:
            #减少一个飞船
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #情空外星人和子弹列表
            self.aliens.empty()
            self.bullets.empty()

            #创建一个新的外星舰队，把飞船放在屏幕底部中间
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _create_fleet(self):
        """创建alien舰队"""
        #创建一个外星人,并不断添加，直到没有空间
        #间距为外星人的宽度和高度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < self.setting.screen_height - 3*alien_height:
            while current_x < (self.setting.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width

            current_x = alien_width
            current_y += 2*alien_height


    def _create_alien(self,x_pos,y_pos):
        """创建一个外星人放在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)  # type:ignore


    def _check_fleet_edge(self):
        """有外星人到达边缘时采取措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """下移整个外星舰队，并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.alien_drop_speed
        self.setting.alien_direction *= -1


    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            #退出程序
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            #发射子弹
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)

            #飞船移动
        keys = pygame.key.get_pressed()
        self.ship.moving_right = keys[pygame.K_d]
        self.ship.moving_left = keys[pygame.K_a]
        self.ship.moving_up = keys[pygame.K_w]
        self.ship.moving_down = keys[pygame.K_s]


    def _check_play_button(self,mouse_pos):
        """再点击play按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #还原游戏设置
            self.setting.initialize_dynamic_settings()
            #重置游戏统计信息
            self.stats.reset_stats()
            self.game_active = True
            self.sb.prep_score()
            self.sb.prep_ships()

            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            #创建新的舰队并放在屏幕中间
            self._create_fleet()
            self.ship.center_ship()

            #隐藏光标
            pygame.mouse.set_visible(False)


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
        self.aliens.draw(self.screen)
        #显示得分
        self.sb.show_score()

        #如果游戏处于非活动状态,就绘制Play按钮
        if not self.game_active:
            self.play_button.draw_botton()

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