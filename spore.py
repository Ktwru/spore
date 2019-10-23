import pygame
import copy
from random import randint
import math

pygame.init()


def main():
    window = pygame.display.set_mode((850, 600))
    window.fill((0, 0, 0))

    field_matrix = [[0 for x in range(100)] for y in range(100)]
    field_matrix[20][20] = 1
    for i in range(100):
        field_matrix[randint(1, 99)][randint(1, 99)] = 2
    field_surface = pygame.Surface((500, 500))
    side = [1000]

    pygame.display.update()
    while True:
        pygame.time.delay(100)
        window.fill((0, 0, 0))
        field_surface.fill((0, 0, 0))
        field_matrix_copy = copy.deepcopy(field_matrix)
        xseed = randint(1, 99)
        yseed = randint(1, 99)
        if field_matrix[yseed][xseed] != 1:
            field_matrix[yseed][xseed] = 2

        for y in range(50):
            for x in range(50):
                if field_matrix_copy[y][x] == 1:
                    if field_matrix[y-1][x] != 1 or field_matrix[y+1][x] != 1 or field_matrix[y][x+1] != 1 or field_matrix[y][x-1] != 1:
                        pygame.draw.rect(field_surface, (0, 28, 89), (x * 10, y * 10, 10, 10))
                    elif field_matrix[y - 3][x] == 1 and field_matrix[y + 3][x] == 1 and field_matrix[y][x + 3] == 1 and field_matrix[y][x - 3] == 1:
                        pygame.draw.rect(field_surface, (0, 80, 255), (x * 10, y * 10, 10, 10))
                    else:
                        pygame.draw.rect(field_surface, (0, 62, 196), (x * 10, y * 10, 10, 10))
                elif field_matrix[y][x] == 2:
                    pygame.draw.rect(field_surface, (0, 135, 72), (x * 10, y * 10, 10, 10))

        for y in range(50):
            for x in range(50):
                if field_matrix_copy[y][x] == 1:
                    if x not in (-1, 492) and y not in (-1, 492):
                        if field_matrix[y-1][x] != 1 or field_matrix[y+1][x] != 1 or field_matrix[y][x+1] != 1 or field_matrix[y][x-1] != 1:
                            for ydif in range(-20, 20):
                                for xdif in range(-20, 20):
                                    if field_matrix[y + ydif][x + xdif] == 2:
                                        if (ydif*ydif) + (xdif*xdif) < side[0]:
                                            if math.fabs(ydif) <= math.fabs(xdif):
                                                if xdif < 0:
                                                    side = [(ydif*ydif) + (xdif*xdif), y, x - 1]
                                                else:
                                                    side = [(ydif*ydif) + (xdif*xdif), y, x + 1]
                                            else:
                                                if ydif < 0:
                                                    side = [(ydif*ydif) + (xdif*xdif), y - 1, x]
                                                else:
                                                    side = [(ydif*ydif) + (xdif*xdif), y + 1, x]
        print(side)
        field_matrix[side[1]][side[2]] = 1
        if side[0] == 1:
            side[0] = 10000


        window.blit(field_surface, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
