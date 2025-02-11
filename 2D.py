import pygame
import sys
import math
pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformation")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def translation(x1, y1, x2, y2, tx, ty):
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 5)
    x11, y11 = x1 + tx, y1 + ty
    x22, y22 = x2 + tx, y2 + ty
    pygame.draw.line(screen, YELLOW, (x11, y11), (x22, y22), 5)

def scaling(x1, y1, x2, y2, sx, sy):
    x22 = x1 + (x2 - x1) * sx
    y22 = y1 + (y2 - y1) * sy
    pygame.draw.line(screen, GREEN, (x1, y1), (x22, y22), 5)

def rotation(x1, y1, x2, y2, angle):
    rad = math.radians(angle)
    x_rel = x2 - x1
    y_rel = y2 - y1
    x_rot = x_rel * math.cos(rad) - y_rel * math.sin(rad)
    y_rot = x_rel * math.sin(rad) + y_rel * math.cos(rad)
    x22 = x1 + x_rot
    y22 = y1 + y_rot
    pygame.draw.line(screen, BLUE, (x1, y1), (x22, y22), 5)
def main():
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        translation(300, 200, 500, 300, 200, 200)
        scaling(300, 200, 500, 300, 2, 2)
        rotation(300, 200, 500, 300, 45)
        pygame.display.flip()
  

if __name__ == "__main__":
    main()
