import pygame
import random



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        moleSquareX = 0
        moleSquareY = 0

        screen = pygame.display.set_mode((640, 512))

        clock = pygame.time.Clock()
        running = True

        while running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: # check if you clicked
                    x, y = event.pos
                    x //= 32
                    y //= 32
                    if x == moleSquareX and y == moleSquareY: # check if click is equal to mole pos
                        moleSquareY = random.randint(0,15)
                        moleSquareX = random.randint(0, 19)

            screen.fill("light green")
            # drawlines
            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (0, i * 32),
                    (640, i * 32),
                    1
                )

            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (i * 32, 0),
                    (i * 32, 512),

                    1
                )

            screen.blit(mole_image, mole_image.get_rect(topleft=(moleSquareX*32, moleSquareY*32)))


            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
    print("testforGit")
