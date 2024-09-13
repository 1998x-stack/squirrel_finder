# player.py

import pygame  # 导入pygame库
from entity import Entity  # 从entity模块导入Entity类
from config import SCREEN_WIDTH, SCREEN_HEIGHT  # 从config模块导入屏幕宽度和高度常量

class Player(Entity):  # 定义Player类，继承自Entity
    """玩家类，代表考拉。"""
    def __init__(self, image):  # 初始化方法
        super().__init__(image)  # 调用父类的初始化方法
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # 设置玩家初始位置为屏幕中心
        self.speed = 5  # 设置玩家移动速度

    def handle_keys(self, keys_pressed):  # 处理按键输入的方法
        """通过方向键处理玩家移动。"""
        if keys_pressed[pygame.K_LEFT]:  # 如果按下左方向键
            self.rect.x -= self.speed  # 向左移动
        if keys_pressed[pygame.K_RIGHT]:  # 如果按下右方向键
            self.rect.x += self.speed  # 向右移动
        if keys_pressed[pygame.K_UP]:  # 如果按下上方向键
            self.rect.y -= self.speed  # 向上移动
        if keys_pressed[pygame.K_DOWN]:  # 如果按下下方向键
            self.rect.y += self.speed  # 向下移动

        # 保持玩家在屏幕范围内
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))  # 限制x坐标范围
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))  # 限制y坐标范围