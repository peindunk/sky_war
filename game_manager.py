# -*-coding:utf-8-*-
import pygame
import player
import enemy

def main():
    screen = pygame.display.set_mode((480, 850), 0, 32)
    background = pygame.image.load("./feiji/background.jpg")
    pygame.display.set_caption('特级制作的飞机大战')

    hero = player.Player(screen)

    enemy_obj = enemy.EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy_obj.display()
        enemy_obj.move()
        pygame.display.update()
        player.key_control(hero)
        for item in hero.bullet_list:
            item.collider_detection(enemy_obj)
if __name__ == "__main__":
    main()


