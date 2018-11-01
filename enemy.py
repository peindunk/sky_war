# -*-coding:utf-8-*-
import pygame

class EnemyPlane:
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.screen = screen_temp
        self.direction = "right"
        # self.rect = self.image.get_rect()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"