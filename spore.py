import pygame
import copy

pygame.init()


def main():
    window = pygame.display.set_mode((850, 600))
    window.fill((0, 0, 0))

    field_matrix = [[0 for x in range(100)] for y in range(100)]
    field_matrix[20][20] = 1
    field_surface = pygame.Surface((500, 500))

    pygame.display.update()
    while True:
        pygame.time.delay(30)
        window.fill((0, 0, 0))
        field_surface.fill((0, 0, 0))
        field_matrix_copy = copy.deepcopy(field_matrix)

        for y in range(100):
            for x in range(100):
                if field_matrix_copy[y][x] == 1:
                    pygame.draw.rect(field_surface, (255, 255, 255), (x*5, y*5, 5, 5))
                    if x not in (0, 99) and y not in (0, 99):
                        field_matrix[y-1][x] = 1
                        field_matrix[y][x-1] = 1
                        field_matrix[y+1][x] = 1
                        field_matrix[y][x+1] = 1
        window.blit(field_surface, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
