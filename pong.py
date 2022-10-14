import pygame, sys

# Начальные настройки библиотеки PyGame
pygame.init()
clock = pygame.time.Clock()

# Настройки главного окна
screen_width = 1280
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

while True:
    # Главный игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление окна
    pygame.display.flip()
    clock.tick(60)