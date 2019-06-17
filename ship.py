import pygame



class Ship():

    def __init__(self,ai_settings,screen):
            self.screen = screen
            self.ai_settings = ai_settings
            '''加载飞船图像并获取其外接矩形    rect 表示属性'''
            self.image = pygame.image.load('images/ship.bmp')
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            '''将飞船放在屏幕底部中央 设置图像位置'''
            self.rect.x = self.screen_rect.centerx  # 图像中心x轴的=屏幕的x轴
            self.rect.bottom = self.screen_rect.bottom   # 图像y轴=屏幕下方的y轴
            self.moving_right = False
            self.moving_left = False
            """在飞船属性center中储存小数值"""
            self.center = float(self.rect.x)
    def blitme(self):
            # 在指定位置绘制飞船
            self.screen.blit(self.image,self.rect)
    def update(self):
            """根据移动标志调整飞船位置"""
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
                #根据self.center更新rect对象
            self.rect.x = self.center





