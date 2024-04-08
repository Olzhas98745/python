import pygame
pygame.init()

# Set up the screen dimensions
screen = pygame.display.set_mode((1080, 900))
pygame.display.set_caption("PAINT")

# Initialize the game clock
clock = pygame.time.Clock()

# Define color constants
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

# Load and scale the eraser image
eraser = pygame.image.load('eraser.png')
eraser = pygame.transform.scale(eraser, (70, 70))

# Function to draw colored rectangles for color selection
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

# Function to draw a rhombus shape
def draw_rhombus():
    pygame.draw.polygon(screen, WHITE, ((20, 65), (0, 85), (20, 105), (40, 85)), 4)

# Function to draw a right triangle shape
def draw_righttr():
    pygame.draw.polygon(screen, WHITE, ((0, 115), (0, 155), (40, 155)), 4)

# Function to draw an equilateral triangle shape
def draw_eqtr():
    pygame.draw.polygon(screen, WHITE, ((20, 175), (0, 209.6), (40, 209.6)), 4)

# Function to pick the current drawing color or shape based on mouse position
def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return BLUE
        elif 1010 <= x <= 1080 and 0 <= y <= 40:
            return BLACK
        elif 130 <= x <= 170 and 0 <= y <= 40:
            return "rect"
        elif 0 <= x < +40 and 65 <= y <= 105:
            return "rhombus"
        elif 0 <= x <= 40 and 115 <= y <= 155:
            return "rtr"
        elif 0 <= x <= 40 and 175 <= y <= 209.6:
            return "eqtr"
    return color

# Function to handle painting shapes on the screen
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color == 'rect':
            pygame.draw.rect(screen, WHITE, (x, y, 40, 40), 4)
        elif color == 'rhombus':
            pygame.draw.polygon(screen, WHITE, ((x, y), (x-20, y+20), (x, y+40), (x+20, y+20)), 4)
        elif color == 'rtr':
            pygame.draw.polygon(screen, WHITE, ((x, y), (x, y+40), (x+40, y+40)), 4)
        elif color == 'eqtr':
            pygame.draw.polygon(screen, WHITE, ((x, y), (x-20, y+35), (x+20, y+35)), 4)
        else:
            pygame.draw.circle(screen, color, (x, y), 27)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Draw color selection rectangles and shapes
    for i in range(len(colors)):
        draw_rect(i)
    draw_rhombus()
    draw_righttr()
    draw_eqtr()
    screen.blit(eraser, (1010, 0))
    pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 4)

    # Get the current drawing color or shape
    color = pick_color()

    # Handle painting on the screen
    painting(color)

    # Control the frame rate
    clock.tick(370)
    pygame.display.update()
