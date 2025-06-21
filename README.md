1. Инициализация Pygame и установка экрана
python
Copy
Edit
import pygame, sys, time
pygame.init()
WIDTH, HEIGHT = 1300, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('Arial', 24, bold=True)
pygame.init() — инициализация всех модулей Pygame.

WIDTH, HEIGHT — размеры окна.

screen — объект окна.

clock — для контроля FPS (кадров в секунду).

FONT — шрифт (не используется в коде, но можно использовать для текста).

🖼️ 2. Загрузка изображений
python
Copy
Edit
background = pygame.image.load("background.png")
parts = [pygame.image.load(f"part{i+1}.png").convert_alpha() for i in range(7)]
reference_image = pygame.image.load("assembly.gif").convert_alpha()
Загружается фон background.

Загружаются 7 частей машины в список parts[0]...parts[6].

Загружается эталонное изображение reference_image (например, правильная сборка).

📍 3. Начальные позиции и переменные
python
Copy
Edit
positions = [[620, 700], [150, 400], ..., [470, 490]]
tolerances = [0, 40, 140, 340, 340, 340, 340]
dragging = [False] * 7
assembled_offset = [0] * 7
assembled_y = [0] * 7
assembled = False
animate = False
selected = None
body_x = 0
positions — координаты каждой части и последней (образца).

tolerances — допустимые отклонения для проверки правильной сборки.

dragging — список, показывающий, какие части перетаскиваются.

assembled_offset, assembled_y — сохраняют смещения после сборки.

assembled, animate — логические флаги.

selected — индекс выбранной (перетаскиваемой) части.

body_x — координата "тела" машины, для анимации.

🌀 4. Главный цикл
python
Copy
Edit
while running:
Обрабатывает события, рисует графику, запускает анимацию.

🖱️ 5. Обработка событий
python
Copy
Edit
for event in pygame.event.get():
Обрабатываются все события:

QUIT: выход из игры.

MOUSEBUTTONDOWN: нажали ЛКМ — проверяется, попала ли мышь по какой-то части.

MOUSEBUTTONUP: отпустили ЛКМ — прекращаем перетаскивание.

MOUSEMOTION: двигаем часть мышью, если она выбрана.

KEYDOWN (SPACE): проверка правильной сборки всех частей (если они в пределах tolerances), и запуск анимации, если всё собрано.

✅ 6. Проверка сборки
python
Copy
Edit
if assembled:
    ...
Проверяются смещения всех частей относительно части 0 (тело).

Если все в пределах tolerances[i], то запоминаются смещения assembled_offset, высоты assembled_y, и начинается движение.

🎞️ 7. Анимация
python
Copy
Edit
if animate:
    body_x -= 2
    if body_x + min(assembled_offset) < -200:
        body_x = WIDTH + max(assembled_offset)
    ...
    time.sleep(0.01)
Двигает машину влево, пока она не исчезнет с экрана.

Как только исчезла — появляется справа.

Смещения assembled_offset и assembled_y используются, чтобы все части двигались как единое целое.

🖼️ 8. Отрисовка
python
Copy
Edit
for i in range(7):
    screen.blit(parts[i], positions[i])
screen.blit(reference_image, positions[7])
pygame.display.flip()
clock.tick(60)
Отрисовываются все 7 частей.

Рядом — эталонное изображение.

Обновляется экран (flip()), ограничение до 60 FPS.

🛑 9. Завершение
python
Copy
Edit
pygame.quit()
sys.exit()
Завершает работу Pygame и закрывает окно.
