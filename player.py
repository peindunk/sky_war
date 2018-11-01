# -*- coding:utf-8 -*-
<<<<<<< HEAD
=======

>>>>>>> 390967f991f343df36bb4046cbcafa735fbfa377
import pygame
import time

class Player:
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.image = pygame.image.load("./feiji/hero1.png")
        self.screen = screen_temp
        self.bullet_list = []

        self.ismove = False
        self.hit = False
        self.speed = 5

    def display(self):
        if self.hit == True:
            time.sleep(1)
            exit()
        else:
            self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
<<<<<<< HEAD
            self.x -= self.speed

    def move_right(self):
            self.x += self.speed

    def move_up(self):
            self.y -= self.speed

    def move_down(self):
            self.y += self.speed
=======
        if self.ismove:
            self.x -= 8

    def move_right(self):
        if self.ismove:
            self.x += 8

    def move_up(self):
        if self.ismove:
            self.y -= 8

    def move_down(self):
        if self.ismove:
            self.y += 8
>>>>>>> 390967f991f343df36bb4046cbcafa735fbfa377

    def fire(self):
        bullet = PlayerBullet(self.screen, self.x, self.y)
        self.bullet_list.append(bullet)

<<<<<<< HEAD
import pygame.sprite
=======
>>>>>>> 390967f991f343df36bb4046cbcafa735fbfa377
class PlayerBullet:
    def __init__(self, screen_temp, x_temp, y_temp):
        self.x = x_temp + 50
        self.y = y_temp - 20
        self.image = pygame.image.load("./feiji/bullet.png")
        self.screen = screen_temp
        # self.rect = self.image.get_rect()

    def collider_detection(self,other):
        pass


    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 4

def key_control(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit")
            exit()
<<<<<<< HEAD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
=======
        elif event.type == pygame.KEYDOWN:
            player.ismove = True
            if event.key == pygame.K_LEFT and player.x > 0:
                print('left')
                player.move_left()
            elif event.key == pygame.K_RIGHT and player.x < 360:
                print('right')
                player.move_right()
            elif event.key == pygame.K_UP and player.y > 0:
                print('UP')
                player.move_up()
            elif event.key == pygame.K_DOWN and player.y < 750:
                print('down')
                player.move_down()
            elif event.key == pygame.K_SPACE:
>>>>>>> 390967f991f343df36bb4046cbcafa735fbfa377
                print('space')
                player.fire()
            elif event.key == pygame.K_ESCAPE:
                exit()

    press_key = pygame.key.get_pressed()
    if press_key[pygame.K_UP] and player.y > 0:
        print('UP')
        player.move_up()
    elif press_key[pygame.K_LEFT] and player.x > 0:
        print('left')
        player.move_left()
    elif press_key[pygame.K_RIGHT] and player.x < 360:
        print('right')
        player.move_right()
    elif press_key[pygame.K_DOWN] and player.y < 750:
        print('down')
        player.move_down()
