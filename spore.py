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
    field_matrix[23][23] = 2
    field_surface = pygame.Surface((500, 500))
    side = [1000]
    tic = 0
    feed = 1
    font = pygame.font.Font('PixelFont.ttf', 36)
    free = 5

    pygame.display.update()
    while True:
        pygame.time.delay(30)
        window.fill((20, 0, 0))
        field_surface.fill((0, 0, 0))
        field_matrix_copy = copy.deepcopy(field_matrix)
        tic += 1
        t_feed = font.render('score:' + str(free), 0, (0, 135, 72))
        t_side = font.render('side:' + str(side), 0, (0, 135, 72))
        window.blit(t_feed, (600, 50))
        window.blit(t_side, (600, 100))

        if tic == 1:                    # food spawn
            xseed = randint(6, 44)
            yseed = randint(6, 44)
            if field_matrix[yseed][xseed] != 1:
                field_matrix[yseed][xseed] = 2
        elif tic == 10:
            tic = 0

        for y in range(50):                # viasualisation
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

        for y in range(50):                 # eating
            for x in range(50):
                if field_matrix_copy[y][x] == 1:
                    if field_matrix[y-1][x] != 1 or field_matrix[y+1][x] != 1 or field_matrix[y][x+1] != 1 or field_matrix[y][x-1] != 1:
                        for ydif in range(-5, 5):
                            for xdif in range(-5, 5):
                                if field_matrix[y + ydif][x + xdif] == 2:
                                    if (ydif*ydif) + (xdif*xdif) < side[0]:
                                        if math.fabs(ydif) < math.fabs(xdif):
                                            if xdif < 0:
                                                side = [(ydif*ydif) + (xdif*xdif), y, x - 1]
                                            else:
                                                side = [(ydif*ydif) + (xdif*xdif), y, x + 1]
                                        else:
                                            if ydif < 0:
                                                side = [(ydif*ydif) + (xdif*xdif), y - 1, x]
                                            else:
                                                side = [(ydif*ydif) + (xdif*xdif), y + 1, x]
        print(side, feed)
        field_matrix[side[1]][side[2]] = 1

        if side[0] == 1:
            side[0] = 10001
            feed += 1
            free += 10
        circuit = []             # growing up
        for y in range(50):
            for x in range(50):
                if field_matrix_copy[y][x] == 1:
                    if field_matrix[y - 1][x] != 1:
                        circuit.append([y - 1, x])
                    if field_matrix[y + 1][x] != 1:
                        circuit.append([y + 1, x])
                    if field_matrix[y][x + 1] != 1:
                        circuit.append([y, x + 1])
                    if field_matrix[y][x - 1] != 1:
                        circuit.append([y, x - 1])
        if free != 0:
            cords = circuit[randint(0, len(circuit) - 1)]
            field_matrix[cords[0]][cords[1]] = 1
            free -= 1

        window.blit(field_surface, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                field_matrix[pos[1] // 10][pos[0] // 10] = 2



if __name__ == "__main__":
    main()
