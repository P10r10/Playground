import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption("My window!")
spider = pygame.image.load("spider.bmp")
spider_rect = spider.get_rect()
spider_rect.midbottom = screen_rect.midbottom
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 255))
    screen.blit(spider, spider_rect)
    pygame.display.flip()
