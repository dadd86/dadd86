import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rompe las cajas')

# Colores
COLORS = [
    (255, 0, 0),    # Rojo
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
    (255, 255, 0),  # Amarillo
    (255, 165, 0),  # Naranja
    (0, 255, 255)   # Cian
]

# Dimensiones de las cajas
BOX_SIZE = 40
MARGIN = 5

# Configuración inicial
boxes = []
colors = random.sample(COLORS * 20, 100)  # 100 cajas con colores aleatorios

# Función para crear las cajas
def create_boxes():
    global boxes
    boxes = []
    color_index = 0
    for row in range(10):
        for col in range(10):
            box = pygame.Rect(col * (BOX_SIZE + MARGIN), row * (BOX_SIZE + MARGIN), BOX_SIZE, BOX_SIZE)
            boxes.append({'rect': box, 'color': colors[color_index]})
            color_index += 1

# Función para dibujar las cajas
def draw_boxes():
    for box in boxes:
        if box['color'] != (0, 0, 0):  # Si la caja no está "rota" (color negro)
            pygame.draw.rect(screen, box['color'], box['rect'])

# Función para romper una caja
def break_box(pos):
    for box in boxes:
        if box['rect'].collidepoint(pos) and box['color'] != (0, 0, 0):
            box['color'] = (0, 0, 0)  # Cambiar a color negro para simular que está rota

# Función para cambiar de color cuando todas las cajas de un color estén rotas
def change_color(current_color):
    for box in boxes:
        if box['color'] == current_color:
            return False
    return True

# Juego principal
running = True
current_color = colors[0]  # Inicializamos el color actual con el primero en la lista aleatoria
create_boxes()

while running:
    screen.fill((255, 255, 255))  # Fondo blanco

    # Dibujar las cajas
    draw_boxes()

    # Comprobar si se debe cambiar el color
    if change_color(current_color):
        # Cambiar al siguiente color
        next_color_index = (colors.index(current_color) + 1) % len(COLORS)
        current_color = colors[next_color_index]
        # Reempezar el juego
        create_boxes()

    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                break_box(event.pos)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
