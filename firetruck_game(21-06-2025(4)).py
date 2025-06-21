import pygame, sys, time

pygame.init()
WIDTH, HEIGHT = 1300, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('Arial', 24, bold=True)

# Загрузка фона и частей машины
background = pygame.image.load("background.png")
parts = [pygame.image.load(f"part{i+1}.png").convert_alpha() for i in range(7)]
reference_image = pygame.image.load("assembly.gif").convert_alpha()

# Начальные позиции
positions = [[620, 700], [150, 400], [100, 600],[200, 800], [350, 550], [250, 820],
    [800, 300], [470, 490]]  # последняя — reference

tolerances = [0, 40, 140, 340, 340, 340, 340]
dragging = [False] * 7
assembled_offset = [0] * 7
assembled_y = [0] * 7

assembled = False
animate = False
selected = None
body_x = 0  # логическая координата "тела" машины

running = True
while running:
    screen.fill('gold')
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(7):
                x, y = positions[i]
                rect = parts[i].get_rect(topleft=(x, y))
                if rect.collidepoint(event.pos):
                    dragging[i] = True
                    selected = i
                    break

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if selected is not None:
                dragging[selected] = False
                selected = None

        elif event.type == pygame.MOUSEMOTION and selected is not None:
            img = parts[selected]
            mx, my = event.pos
            positions[selected][0] = mx - img.get_width() // 2
            positions[selected][1] = my - img.get_height() // 2

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            base_x, base_y = positions[0]  # тело машины — часть 0
            assembled = True
            for i in range(1, 7):
                dx = positions[i][0] - base_x
                dy = positions[i][1] - base_y
                if abs(dx) > tolerances[i] or abs(dy) > tolerances[i]:
                    assembled = False
                    break
            if assembled:
                for i in range(7):
                    assembled_offset[i] = positions[i][0] - base_x
                    assembled_y[i] = positions[i][1]
                body_x = base_x
                animate = True

    if animate:
        body_x -= 2  # движение влево
        if body_x + min(assembled_offset) < -200:
            body_x = WIDTH + max(assembled_offset)  # вернуть вправо
        for i in range(7):
            positions[i][0] = body_x + assembled_offset[i]
            positions[i][1] = assembled_y[i]
        time.sleep(0.01)

    # Отрисовка всех изображений
    for i in range(7):
        screen.blit(parts[i], positions[i])
    screen.blit(reference_image, positions[7])  # последняя — образец

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
