# main.py

import pygame  # 导入pygame库
from game import Game  # 从game模块导入Game类
from config import *  # 从config模块导入所有变量
from logger import log_event  # 从logger模块导入log_event函数

# 初始化pygame
pygame.init()

# 设置屏幕和字体
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 创建游戏窗口
pygame.display.set_caption("Squirrel Finder")  # 设置窗口标题
FONT = pygame.font.SysFont('arial', FONT_SIZE)  # 设置字体

# 加载资源
PLAYER_IMG = pygame.image.load(KOALA_IMG_PATH)  # 加载玩家图像
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (40, 40))  # 调整玩家图像大小

STRAWBERRY_IMG = pygame.image.load(STRAWBERRY_IMG_PATH)  # 加载草莓图像
STRAWBERRY_IMG = pygame.transform.scale(STRAWBERRY_IMG, (40, 40))  # 调整草莓图像大小

SQUIRREL_IMG = pygame.image.load(SQUIRREL_IMG_PATH)  # 加载松鼠图像
SQUIRREL_IMG = pygame.transform.scale(SQUIRREL_IMG, (40, 40))  # 调整松鼠图像大小

# 加载音效
WIN_SOUND = pygame.mixer.Sound(WIN_SOUND_PATH)  # 加载胜利音效
LOSE_SOUND = pygame.mixer.Sound(LOSE_SOUND_PATH)  # 加载失败音效

# 记录游戏初始化日志
log_event("Game initialized")  # 记录游戏初始化事件

# 启动游戏
if __name__ == "__main__":  # 如果这个脚本是主程序
    game = Game(PLAYER_IMG, STRAWBERRY_IMG, SQUIRREL_IMG, WIN_SOUND, LOSE_SOUND, FONT, SCREEN)  # 创建Game实例
    game.run()  # 运行游戏