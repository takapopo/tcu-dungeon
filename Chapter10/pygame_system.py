import pygame
import sys

WHITE = (255, 200, 200)
BLACK = (  0,   0,   0)

def main():
    pygame.init()
    pygame.display.set_caption("Pygame")
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 3)
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        txt = font.render(str(tmr), True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt, [300, 200])
        pygame.display.update()
        clock.tick(144)

if __name__ == '__main__':
    main()
