import pygame
class Enemy:
    def __init__(self, enemy_x, enemy_y, size_x, size_y, hp, color):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.size_x = size_x
        self.size_y = size_y
        self.hp = hp
        self.color = color
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.enemy_x, self.enemy_y, self.size_x, self.size_y))
    def border(self):
        pass
