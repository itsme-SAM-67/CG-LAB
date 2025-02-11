import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Algorithm")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0 )
def draw_circle(screen, x_center, y_center, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        screen.set_at((x_center + x, y_center + y), WHITE)
        screen.set_at((x_center - x, y_center + y), "RED")
        screen.set_at((x_center + x, y_center - y), "GREEN")
        screen.set_at((x_center - x, y_center - y), "BLUE")
        screen.set_at((x_center + y, y_center + x), "PURPLE")
        screen.set_at((x_center - y, y_center + x), "ORANGE")
        screen.set_at((x_center + y, y_center - x), "YELLOW ")
        screen.set_at((x_center - y, y_center - x), "cyan")

        x += 1
        if p <= 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        print(x,y, "points")
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_circle(screen, WIDTH // 2, HEIGHT // 2, 100)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()