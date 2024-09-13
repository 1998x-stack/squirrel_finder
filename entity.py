# entity.py
"""
1. 继承关系
```python
class Entity(pygame.sprite.Sprite):
```
Entity类继承自`pygame.sprite.Sprite`。Sprite是Pygame中用于处理移动图像的基类，提供了许多有用的方法和属性，便于碰撞检测和组管理。

2. 初始化方法
```python
def __init__(self, image, delay=0):
```
- `image`参数接收实体的图像。
- `delay`参数设置实体出现前的延迟时间，默认为0。

3. 位置和大小
```python
self.rect = self.image.get_rect()
self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
```
- 使用`get_rect()`方法获取图像的矩形边界。
- 随机设置初始位置，确保实体完全在屏幕内。

4. 速度
```python
self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])
```
随机选择x和y方向的速度，使每个实体的运动都不同。

5. 延迟出现机制
```python
self.delay = delay
self.spawn_time = pygame.time.get_ticks()
```
记录生成时间和延迟时间，用于控制实体的出现时机。

6. 更新方法
```python
def update(self):
```
这个方法在每一帧被调用，用于更新实体的状态。

7. 延迟处理
```python
if self.delay > 0:
    if (current_time - self.spawn_time) < self.delay * 1000:
        return
```
检查是否还在延迟时间内，如果是，则不进行移动。

8. 移动逻辑
```python
self.rect.x += self.speed_x
self.rect.y += self.speed_y
```
根据速度更新实体的位置。

9. 边界碰撞检测
```python
if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
    self.speed_x *= -1
if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
    self.speed_y *= -1
```
检测是否碰到屏幕边界，如果是，则反转相应方向的速度，实现反弹效果。

技术要点：
1. 使用Pygame的Sprite系统，便于管理和渲染。
2. 随机初始化位置和速度，增加游戏的随机性和趣味性。
3. 实现了简单的物理系统（速度和反弹）。
4. 使用延迟机制，可以控制实体的出现时机。
5. 边界检测确保实体始终在屏幕内。

这个Entity类为游戏中的所有移动对象提供了一个坚实的基础，可以很容易地扩展以添加更多特定的行为和属性。
"""

import pygame  # 导入pygame库
import random  # 导入random库
from config import SCREEN_WIDTH, SCREEN_HEIGHT  # 从config文件导入屏幕宽度和高度

class Entity(pygame.sprite.Sprite):  # 定义Entity类，继承自pygame.sprite.Sprite
    """Generic class for player and enemies (strawberries and squirrel)."""  # 玩家和敌人（草莓和松鼠）的通用类
    def __init__(self, image, delay=0):  # 初始化方法，接受图像和延迟参数
        super().__init__()  # 调用父类的初始化方法
        self.image = image  # 设置实体的图像
        self.rect = self.image.get_rect()  # 获取图像的矩形边界
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # 随机设置x坐标
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)  # 随机设置y坐标
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])  # 随机选择x方向速度
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])  # 随机选择y方向速度
        self.delay = delay  # 设置出现前的延迟时间（秒）
        self.spawn_time = pygame.time.get_ticks()  # 记录生成时间

    def update(self):  # 更新方法，用于更新实体状态
        current_time = pygame.time.get_ticks()  # 获取当前时间
        if self.delay > 0:  # 如果有延迟
            if (current_time - self.spawn_time) < self.delay * 1000:  # 如果还在延迟时间内
                return  # 不移动，直接返回

        self.rect.x += self.speed_x  # 更新x坐标
        self.rect.y += self.speed_y  # 更新y坐标

        # 碰到墙壁时反弹
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:  # 如果碰到左右边界
            self.speed_x *= -1  # 水平速度反向
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:  # 如果碰到上下边界
            self.speed_y *= -1  # 垂直速度反向