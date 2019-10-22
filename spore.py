import pygame
import copy
from random import randint

pygame.init()


def main():
    window = pygame.display.set_mode((850, 600))
    window.fill((0, 0, 0))

    field_matrix = [[0 for x in range(100)] for y in range(100)]
    field_matrix[20][20] = 1
    spore_size = 1
    field_surface = pygame.Surface((500, 500))

    pygame.display.update()
    while True:
        pygame.time.delay(50)
        window.fill((0, 0, 0))
        field_surface.fill((0, 0, 0))
        field_matrix_copy = copy.deepcopy(field_matrix)
        plus = 0
        spore_size_copy = spore_size
        way = 1

        for y in range(50):
            for x in range(50):
                if field_matrix_copy[y][x] == 1:
                    if field_matrix[y-1][x] == 0 or field_matrix[y+1][x] == 0 or field_matrix[y][x+1] == 0 or field_matrix[y][x-1] == 0:
                        pygame.draw.rect(field_surface, (0, 28, 89), (x * 10, y * 10, 10, 10))
                    elif field_matrix[y - 3][x] == 1 and field_matrix[y + 3][x] == 1 and field_matrix[y][x + 3] == 1 and field_matrix[y][x - 3] == 1:
                        pygame.draw.rect(field_surface, (0, 80, 255), (x * 10, y * 10, 10, 10))
                    else:
                        pygame.draw.rect(field_surface, (0, 62, 196), (x * 10, y * 10, 10, 10))

        for y in range(50):
            for x in range(50):
                if plus <= 4:
                    if field_matrix_copy[y][x] == 1:
                        if x not in (0, 49) and y not in (0, 49):
                            if field_matrix[y-1][x] == 0 or field_matrix[y+1][x] == 0 or field_matrix[y][x-1] == 0 or field_matrix[y][x+1] == 0:
                                chance = randint(1, 4)
                                if way == 1:
                                    field_matrix[y-1][x] = 1
                                if way == 2:
                                    field_matrix[y+1][x] = 1
                                if way == 3:
                                    field_matrix[y][x-1] = 1
                                if way == 4:
                                    field_matrix[y][x+1] = 1
                                plus += 1
                                if way == 4:
                                    way = 1
                                else:
                                    way += 1

        window.blit(field_surface, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
