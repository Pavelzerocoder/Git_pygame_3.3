import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра тир')
icon = pygame.image.load('img/pic_icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость перемещения мишени
target_speed_x = 0.1  # Скорость по оси X
target_speed_y = 0.1  # Скорость по оси Y

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счётчики попаданий и промахов
hits = 0
misses = 0
font = pygame.font.Font(None, 36)  # Шрифт для отображения текста

running = True
while running:
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                # Перемещаем мишень в случайное место после попадания
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                misses += 1
                # Проверка на проигрыш
                if misses >= 3:
                    print("Вы проиграли! Слишком много промахов.")
                    running = False

    # Перемещение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на выход мишени за границы экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x  # Меняем направление по оси X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y  # Меняем направление по оси Y

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение счётчиков
    hits_text = font.render(f"Попадания: {hits}", True, (255, 255, 255))
    misses_text = font.render(f"Промахи: {misses}", True, (255, 255, 255))
    screen.blit(hits_text, (10, 10))
    screen.blit(misses_text, (10, 50))

    # Обновление экрана
    pygame.display.update()

pygame.quit()
