import pygame

pygame.init()


def main():
    window = pygame.display.set_mode((850, 600))
    window.fill((0, 0, 0))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
