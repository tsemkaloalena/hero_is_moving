import random

import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image

pygame.init()
width, height = 300, 300
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


position = 0, 0
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
image = load_image('creature.png')
image = pygame.transform.scale(image, (100, 100))

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("creature.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.x = 0
sprite.rect.y = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                sprite.rect.y += 10
            if pygame.key.get_pressed()[pygame.K_UP]:
                sprite.rect.y -= 10
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                sprite.rect.x -= 10
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                sprite.rect.x += 10
        #     cursor.rect.topleft = event.pos
    screen.fill((255, 255, 255))
    # if pygame.mouse.get_focused():
    all_sprites.draw(screen)
    # all_sprites.update()
    pygame.display.flip()
pygame.quit()


