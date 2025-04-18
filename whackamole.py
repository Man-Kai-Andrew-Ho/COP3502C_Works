import pygame
import random

# Grid settings
CELL_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16

def get_random_position():
    x = random.randrange(0, GRID_WIDTH) * CELL_SIZE
    y = random.randrange(0, GRID_HEIGHT) * CELL_SIZE
    return x, y

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_image = pygame.image.load("mole.png")

        # Start mole at top-left
        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (mole_x <= mouse_x <= mole_x + CELL_SIZE and
                            mole_y <= mouse_y <= mole_y + CELL_SIZE):
                        mole_x, mole_y = get_random_position()

            screen.fill("light green")
            for x in range(20):
                pygame.draw.line(screen, "dark green", (x * 32, 0), (x * 32, 512))
            for y in range(16):
                pygame.draw.line(screen, "dark green", (0, y * 32), (640, y * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
