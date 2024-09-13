# game.py

import pygame  # 导入pygame库
from player import Player  # 从player模块导入Player类
from entity import Entity  # 从entity模块导入Entity类
from config import *  # 从config模块导入所有内容
from logger import log_event  # 从logger模块导入log_event函数

class Game:
    """游戏类，用于处理状态、逻辑和显示。"""
    def __init__(self, player_img, strawberry_img, squirrel_img, win_sound, lose_sound, font, screen):
        self.state = 'start'  # 初始化游戏状态为'start'
        self.all_sprites = pygame.sprite.Group()  # 创建所有精灵的组
        self.strawberries = pygame.sprite.Group()  # 创建草莓精灵的组
        self.squirrel_group = pygame.sprite.Group()  # 创建松鼠精灵的组
        self.player = Player(player_img)  # 创建玩家对象
        self.all_sprites.add(self.player)  # 将玩家添加到所有精灵组中
        self.start_time = 0  # 初始化游戏开始时间
        self.timer = 0  # 初始化计时器
        self.last_strawberry = 0  # 初始化上一个草莓生成的时间
        self.squirrel_spawned = False  # 初始化松鼠是否已生成的标志
        self.win = False  # 初始化胜利标志
        self.lose = False  # 初始化失败标志
        self.player_img = player_img  # 存储玩家图像
        self.strawberry_img = strawberry_img  # 存储草莓图像
        self.squirrel_img = squirrel_img  # 存储松鼠图像
        self.win_sound = win_sound  # 存储胜利音效
        self.lose_sound = lose_sound  # 存储失败音效
        self.font = font  # 存储字体
        self.screen = screen  # 存储屏幕对象

    def reset(self):
        """重置游戏到初始状态。"""
        self.state = 'start'  # 重置游戏状态为'start'
        self.all_sprites.empty()  # 清空所有精灵组
        self.strawberries.empty()  # 清空草莓精灵组
        self.squirrel_group.empty()  # 清空松鼠精灵组
        self.player = Player(self.player_img)  # 重新创建玩家对象
        self.all_sprites.add(self.player)  # 将玩家添加到所有精灵组中
        self.start_time = pygame.time.get_ticks()  # 重置游戏开始时间
        self.timer = 0  # 重置计时器
        self.last_strawberry = pygame.time.get_ticks()  # 重置上一个草莓生成的时间
        self.squirrel_spawned = False  # 重置松鼠是否已生成的标志
        self.win = False  # 重置胜利标志
        self.lose = False  # 重置失败标志
        log_event("Game reset")  # 记录游戏重置事件

    def spawn_strawberry(self):
        """在屏幕上生成一个新的草莓。"""
        if len(self.strawberries) < MAX_STRAWBERRIES:  # 如果草莓数量小于最大值
            strawberry = Entity(self.strawberry_img)  # 创建一个新的草莓实体
            self.all_sprites.add(strawberry)  # 将草莓添加到所有精灵组中
            self.strawberries.add(strawberry)  # 将草莓添加到草莓精灵组中

    def spawn_squirrel(self):
        """在延迟后生成松鼠。"""
        squirrel = Entity(self.squirrel_img)  # 创建一个新的松鼠实体
        self.all_sprites.add(squirrel)  # 将松鼠添加到所有精灵组中
        self.squirrel_group.add(squirrel)  # 将松鼠添加到松鼠精灵组中

    def run(self):
        """主游戏循环。"""
        CLOCK = pygame.time.Clock()  # 创建一个时钟对象
        running = True  # 设置游戏运行标志

        while running:  # 主游戏循环
            CLOCK.tick(FPS)  # 控制游戏帧率
            for event in pygame.event.get():  # 处理所有事件
                if event.type == pygame.QUIT:  # 如果是退出事件
                    running = False  # 停止游戏运行

                if self.state == 'start':  # 如果游戏状态为'start'
                    if event.type == pygame.KEYDOWN:  # 如果有按键按下
                        self.state = 'playing'  # 将游戏状态改为'playing'
                        self.start_time = pygame.time.get_ticks()  # 记录游戏开始时间
                        self.last_strawberry = pygame.time.get_ticks()  # 记录上一个草莓生成的时间
                        log_event("Game started")  # 记录游戏开始事件

            keys_pressed = pygame.key.get_pressed()  # 获取当前按下的所有键

            if self.state == 'playing':  # 如果游戏状态为'playing'
                self.all_sprites.update()  # 更新所有精灵
                self.player.handle_keys(keys_pressed)  # 处理玩家的键盘输入

                current_time = pygame.time.get_ticks()  # 获取当前时间
                if (current_time - self.last_strawberry) >= 1000:  # 如果距离上一个草莓生成已经过去1秒
                    self.spawn_strawberry()  # 生成一个新的草莓
                    self.last_strawberry = current_time  # 更新上一个草莓生成的时间

                if not self.squirrel_spawned and (current_time - self.start_time) >= 3000:  # 如果松鼠还未生成且游戏开始3秒后
                    self.spawn_squirrel()  # 生成松鼠
                    self.squirrel_spawned = True  # 设置松鼠已生成标志

                self.timer = (current_time - self.start_time) // 1000  # 计算游戏时间

                if pygame.sprite.spritecollideany(self.player, self.strawberries):  # 如果玩家碰到了草莓
                    self.state = 'lose'  # 设置游戏状态为'lose'
                    self.lose = True  # 设置失败标志
                    pygame.mixer.Sound.play(self.lose_sound)  # 播放失败音效
                    pygame.time.set_timer(pygame.USEREVENT + 1, 2000)  # 设置一个2秒后的用户事件
                    log_event("Player lost the game")  # 记录玩家失败事件

                if pygame.sprite.spritecollideany(self.player, self.squirrel_group):  # 如果玩家碰到了松鼠
                    self.state = 'win'  # 设置游戏状态为'win'
                    self.win = True  # 设置胜利标志
                    pygame.mixer.Sound.play(self.win_sound)  # 播放胜利音效
                    pygame.time.set_timer(pygame.USEREVENT + 2, 2000)  # 设置一个2秒后的用户事件
                    log_event("Player won the game")  # 记录玩家胜利事件

            elif self.state in ['win', 'lose']:  # 如果游戏状态为'win'或'lose'
                for event in pygame.event.get():  # 处理所有事件
                    if event.type == pygame.USEREVENT + 1 and self.lose:  # 如果是失败后的用户事件
                        self.reset()  # 重置游戏
                    if event.type == pygame.USEREVENT + 2 and self.win:  # 如果是胜利后的用户事件
                        self.reset()  # 重置游戏

            self.screen.fill(BLACK)  # 用黑色填充屏幕

            if self.state == 'start':  # 如果游戏状态为'start'
                instructions = [
                    "Welcome to Squirrel Finder!",
                    "Use arrow keys to move the koala.",
                    "Avoid bouncing strawberries.",
                    "Catch the squirrel to win the game.",
                    "Press any key to start."
                ]
                for idx, line in enumerate(instructions):  # 遍历所有说明文本
                    text = self.font.render(line, True, WHITE)  # 渲染文本
                    self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100 + idx * 40))  # 在屏幕上绘制文本
            else:  # 如果游戏状态不是'start'
                self.all_sprites.draw(self.screen)  # 在屏幕上绘制所有精灵
                openai_text = self.font.render("openai", True, RETRO_GREEN)  # 渲染"openai"文本
                self.screen.blit(openai_text, (10, 10))  # 在屏幕左上角绘制"openai"文本
                timer_text = self.font.render(f"Time: {self.timer} s", True, WHITE)  # 渲染计时器文本
                self.screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))  # 在屏幕右上角绘制计时器文本

                if self.state == 'win':  # 如果游戏状态为'win'
                    win_text = self.font.render("You Win", True, RETRO_GREEN)  # 渲染胜利文本
                    self.screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2))  # 在屏幕中央绘制胜利文本
                elif self.state == 'lose':  # 如果游戏状态为'lose'
                    lose_text = self.font.render("You Loss", True, RETRO_RED)  # 渲染失败文本
                    self.screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2))  # 在屏幕中央绘制失败文本

            pygame.display.flip()  # 更新整个显示屏幕

        pygame.quit()  # 退出pygame