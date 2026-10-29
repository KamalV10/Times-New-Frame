import pygame
import sys
import vars as v
import classes as c

pygame.init()
screen = pygame.display.set_mode((v.SCREEN_WIDTH, v.SCREEN_HEIGHT))
pygame.display.set_caption("Times New Frame")

running = True
clock = pygame.time.Clock()
x, y = v.SCREEN_WIDTH // 2, v.SCREEN_HEIGHT // 2
speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    up_shield_active = keys[pygame.K_b] and keys[pygame.K_w]
    right_shield_active = keys[pygame.K_b] and keys[pygame.K_d]
    down_shield_active = keys[pygame.K_b] and keys[pygame.K_s]
    left_shield_active = keys[pygame.K_b] and keys[pygame.K_a]

    if not keys[pygame.K_b]:
        if keys[pygame.K_UP] or keys[pygame.K_w]: # движение
            y -= speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed

    if keys[pygame.K_t]: # механика ускорения
        speed = 25
    else:
        speed = 5

    if x < 0: # границы
        x = 0
    if x + v.PLAYER_SIZE > v.SCREEN_WIDTH:
        x = v.SCREEN_WIDTH - v.PLAYER_SIZE
    if y < 0:
        y = 0
    if y + v.PLAYER_SIZE > v.SCREEN_HEIGHT:
        y = v.SCREEN_HEIGHT - v.PLAYER_SIZE

    screen.fill((v.BLACK)) # отрисовка
    if up_shield_active: # отрисовка щита
        pygame.draw.rect(screen, v.GREEN, (x, y - 10, v.PLAYER_SIZE, 5)) # щит сверху
    if right_shield_active:
        pygame.draw.rect(screen, v.GREEN, (x + v.PLAYER_SIZE + 5, y, 5, v.PLAYER_SIZE)) # щит справа
    if down_shield_active:
        pygame.draw.rect(screen, v.GREEN, (x, y + v.PLAYER_SIZE + 5, v.PLAYER_SIZE, 5)) # щит снизу
    if left_shield_active:
        pygame.draw.rect(screen, v.GREEN, (x - 10, y, 5, v.PLAYER_SIZE)) # щит слева

    pygame.draw.rect(screen, v.WHITE, (x, y, v.PLAYER_SIZE, v.PLAYER_SIZE)) # отрисовка игрока
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
