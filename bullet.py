import pygame
from pygame.sprite import Sprite


# 设置子弹管理类
class Bullet(Sprite):

    def __int__(self,ai_settings,screen,ship):
        # 用super()继承sprite
        super(Bullet,self).__init__()
        self.screen = screen
        # 在(0,0)处创建一个子弹矩形,在设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_hight)
        self.rect.x = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        """在子弹属性center中储存小数值"""
        self.y = float(self.rect.y)
    

