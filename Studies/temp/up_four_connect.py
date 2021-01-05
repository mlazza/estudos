import numpy as np
import pygame
import math

ROWS = 6
COLUMNS = 7

board = np.zeros((ROWS, COLUMNS))

gameover = False
turn = True #True -> player 1 plays | False -> player 2 plays

SLOT = 70
width = COLUMNS * SLOT
height = (ROWS + 1) * SLOT
size = (width, height)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = ((255, 255, 255))
OFFSET = 70

RADIUS = int(SLOT / 2 - 5)


def draw(board):
    pygame.draw.rect(window, WHITE, (0, 0, width, SLOT))
    for c in range(COLUMNS):
        for r in range(ROWS):
            rect = (c * SLOT, r * SLOT * OFFSET, SLOT, SLOT)
            c1 = (int(c * SLOT + SLOT / 2), int(r * SLOT + OFFSET + SLOT / 2))
            pygame.draw.rect(window, BLUE, rect)
            pygame.draw.circle(window, WHITE, c1, RADIUS)
    for c in range(COLUMNS):
        for r in range(ROWS):
            c2 = (int(c * SLOT + SLOT / 2), height - int(r * SLOT + SLOT / 2))
            if board[r][c] == 1:
                pygame.draw.circle(window, RED, c2, RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(window, GREEN, c2, RADIUS)
    pygame.display.update()


def valid(board, cal):
    return board[ROWS - 1][col] == 0


def drop(board, col, piece):
    for r in range(ROWS):
        if board[r][col] == 0:
            row = r
            break
    board[row][col] = piece


def win(board, piece):
    # horizontal
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True
            # vertical
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True
            # diagonal
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True
            # diagonal.1
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS - 3):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


print(board)
pygame.init()

window = pygame.display.set_mode(size)
pygame.display.set_caption("connect 4")
draw(board)
counter = 0
full_board = False
while not gameover and not full_board:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(window, GRAY, (0, 0, width, SLOT))
            posx = event.pos[0]
            if turn:  # player one turn
                pygame.draw.circle(window, RED, (posx, int(SLOT / 2)), RADIUS)
            else:
                pygame.draw.circle(window, GREEN, (posx, int(SLOT / 2)), RADIUS)

        pygame.display.update

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn: #Player 1
                posx = event.pos[0]
                col = math.floor(posx / SLOT)
                if valid(board, col):
                    drop(board, col, 1)
                elif win(board, 1):
                    print("player 1 won")
                    gameover = True
                turn = False # pass the turn
                counter += 1
            else: #Player 2
                posx = event.pos[0]
                col = math.floor(posx / SLOT)
                if valid(board, col):
                    drop(board, col, 2)
                elif win(board, 2):
                    print("player 2 won")
                    gameover = True
                turn = True # pass the turn
                counter += 1


            print(np.flip(board, 0))
            draw(board)
    if counter == 42:
        print('Jogo empatou')
        break