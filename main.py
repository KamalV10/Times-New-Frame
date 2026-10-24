import pygame
import sys
import vars as v
import classes as c

pygame.init()
screen = pygame.display.set_mode((v.START_WIDTH, v.START_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Times New Frame")

running = True
clock = pygame.time.Clock()
x, y = v.START_WIDTH / 2, v.START_HEIGHT / 2
speed = 5
enemy = c.Enemy(100, 100, 50, 50, 100, v.RED)

while running:
    screen_width, screen_height = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]: # движение
        y -= speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_t]: # механика замедления времени
        clock.tick(1)
        speed = 35
    else:
        clock.tick(60)
        speed = 5

    if x < 0: # границы
        x = 0
    if x + v.BOX_SIZE > screen_width:
        x = screen_width - v.BOX_SIZE
    if y < 0:
        y = 0
    if y + v.BOX_SIZE > screen_height:
        y = screen_height - v.BOX_SIZE

    clock.tick(60)
    screen.fill((v.BLACK))
    pygame.draw.rect(screen, (v.WHITE), (x, y, v.BOX_SIZE, v.BOX_SIZE))
    enemy.render(screen)
    pygame.display.flip()
    
pygame.quit()
sys.exit()
