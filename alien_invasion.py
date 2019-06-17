import sys
import pygame
import game_functions as model
from setings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个飞船
    ship = Ship(ai_settings,screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        model.check_events(ship)
        ship.update()
        model.updata_screen(ai_settings,screen,ship)

run_game()
