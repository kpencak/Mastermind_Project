import pygame, sys, random, os
from pygame.locals import *

#---------------------------------------------------
pygame.init()

width = 500
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mastermind by Katarzyna Pencak // 2018")
font = pygame.font.SysFont("Purisa", 20)
clock = pygame.time.Clock()
delta = clock.tick(10)
BLUE = (0, 0, 150)

#---------------------------------------------------
class Button(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image)
    def setCords(self,x,y):
        self.rect.topleft = x,y
        screen.blit(self.image, (x,y))
    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0] and mouse[1] > self.rect.topleft[1]:
            if mouse[0] < self.rect.bottomright[0] and mouse[1] < self.rect.bottomright[1]:
                return True
            else:
                return False
        else:
            return False

def draw():
    colors = ["w", "r", "y", "b", "g", "p"]
    solution = [random.choice(colors) for i in range(4)]
    return solution
#---------------------------------------------------
class Board():
    def __init__(self):
        self.board = ["o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o",
                      "o o o o"]

        self.help_board = ["o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o",
                           "o o o o"]

        self.guess_board = ["o", "o", "o", "o"]

        self.white = Button('white.png')
        self.red = Button('red.png')
        self.yellow = Button('yellow.png')
        self.green = Button('green.png')
        self.blue = Button('blue.png')
        self.purple = Button('purple.png')

    def draw_board(self):
        self.board_x = 80
        self.board_y = 80
        for row in self.board:
            pygame.display.update()
            for blank_space in row:
                pygame.display.flip()
                if blank_space == "o":
                    screen.blit(blank, (self.board_x, self.board_y))
                elif blank_space == "w":
                    screen.blit(white, (self.board_x, self.board_y))
                elif blank_space == "r":
                    screen.blit(red, (self.board_x, self.board_y))
                elif blank_space == "y":
                    screen.blit(yellow, (self.board_x, self.board_y))
                elif blank_space == "g":
                    screen.blit(green, (self.board_x, self.board_y))
                elif blank_space == "b":
                    screen.blit(blue, (self.board_x, self.board_y))
                elif blank_space == "p":
                    screen.blit(purple, (self.board_x, self.board_y))
                else:
                    continue
                pygame.display.update()
                self.board_x += 40
            self.board_y += 40
            self.board_x = 80
            pygame.display.flip()

    def draw_help_board(self):
        self.board_x = 10
        self.board_y = 95
        for row in self.help_board:
            for blank_space in row:
                if blank_space == "o":
                    screen.blit(blanky, (self.board_x, self.board_y))
                elif blank_space == "w":
                    screen.blit(bluey, (self.board_x, self.board_y))
                elif blank_space == "b":
                    screen.blit(blacky, (self.board_x, self.board_y))
                else:
                    continue
                pygame.display.update()
                self.board_x += 13
            self.board_y += 40
            self.board_x = 10
            pygame.display.flip()

    def colors(self):
        self.board_x = 350
        self.board_y = 250
        self.white.setCords(self.board_x, self.board_y)
        self.red.setCords(self.board_x+40, self.board_y)
        self.yellow.setCords(self.board_x, self.board_y+40)
        self.green.setCords(self.board_x+40, self.board_y+40)
        self.blue.setCords(self.board_x, self.board_y+80)
        self.purple.setCords(self.board_x+40, self.board_y+80)
        pygame.display.update()

    def check(self, guess_board, turn):
        self.match = []
        self.blacky = 0
        self.blank = []
        if len(self.match) < 4:
            for i in range (len(solution)):
                if i not in self.blank:
                    if guess_board[i] == solution[i]:
                        self.match.append("b")
                        self.blacky += 1
                        self.blank.append(i)
                    else:
                        for j in range(len(solution)):
                            if guess_board[i] == solution[j]:
                                if j not in self.blank:
                                    self.match.append("w")
                                    self.blank.append(j)
                                    break
                                elif j in self.blank and j == 3:
                                    self.match.append("o")
                            elif guess_board[i] != solution[j] and j == 3:
                                self.match.append("o")
                else:
                    for j in range (len(solution)):
                        if guess_board[i] == solution[j]:
                            if j not in self.blank:
                                self.match.append("w")
                                self.blank.append(j)
                                break
                            else:
                                continue
                        elif guess_board[i] != solution[j] and j == 3:
                            self.match.append("o")
                            break
            self.help_board[turn] = self.match

    def solution(self, solution):
        self.board_x = 180
        self.board_y = 400
        for blank_space in solution:
            pygame.display.flip()
            if blank_space == "o":
                screen.blit(blank, (self.board_x, self.board_y))
            elif blank_space == "w":
                screen.blit(white, (self.board_x, self.board_y))
            elif blank_space == "r":
                screen.blit(red, (self.board_x, self.board_y))
            elif blank_space == "y":
                screen.blit(yellow, (self.board_x, self.board_y))
            elif blank_space == "g":
                screen.blit(green, (self.board_x, self.board_y))
            elif blank_space == "b":
                screen.blit(blue, (self.board_x, self.board_y))
            elif blank_space == "p":
                screen.blit(purple, (self.board_x, self.board_y))
            else:
                continue
            self.board_x += 40
        pygame.display.update()

#---------------------------------------------------
# LOADING IMAGES
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', name)
        raise SystemExit
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#--------------------------------------------------
# LOADING IMAGES
blank, blank_rect = load_image('blank.png')
white, white_rect = load_image('white.png')
red, red_rect = load_image('red.png')
yellow, yellow_rect = load_image('yellow.png')
green, green_rect = load_image('green.png')
blue, blue_rect = load_image('blue.png')
purple, purple_rect = load_image('purple.png')
blanky, blanky_rect = load_image('blanky.png')
bluey, bluey_rect = load_image('bluey.png')
blacky, blacky_rect = load_image('blacky.png')
bg_run = pygame.image.load('data/bg_run.png')
bg_main = pygame.image.load('data/bg_main.png')
bg_game = pygame.image.load('data/bg_game.png')
bg_win = pygame.image.load('data/bg_win.png')
bg_lose = pygame.image.load('data/bg_lose.png')
bg_help = pygame.image.load('data/bg_help.png')

#---------------------------------------------------
# GAME
def run():
    screen.blit(bg_run, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                else:
                    main_menu()
        pygame.display.update()

#----------------------------------------------------
def main_menu():
    screen.blit(bg_main, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    ai_vs_p()
                elif event.key == pygame.K_h:
                    help()
                else:
                    break
        pygame.display.update()

#----------------------------------------------------
def ai_vs_p():
    screen.blit(bg_game, (0, 0))
    board = Board()
    global solution
    solution = draw()
    print(solution)

    turn = 0
    board.draw_board()
    board.draw_help_board()
    board.colors()
    tries = 0

    while turn <= 9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                main_menu()
            elif event.type == MOUSEBUTTONDOWN and tries < 4:
                pos = pygame.mouse.get_pos()

                if board.white.pressed(pos) == True:
                    board.guess_board[tries] = "w"
                    board.draw_board()
                    tries += 1

                elif board.red.pressed(pos) == True:
                    board.guess_board[tries] = "r"
                    board.draw_board()
                    tries += 1

                elif board.yellow.pressed(pos) == True:
                    board.guess_board[tries] = "y"
                    board.draw_board()
                    tries += 1

                elif board.green.pressed(pos) == True:
                    board.guess_board[tries] = "g"
                    board.draw_board()
                    tries += 1

                elif board.blue.pressed(pos) == True:
                    board.guess_board[tries] = "b"
                    board.draw_board()
                    tries += 1

                elif board.purple.pressed(pos) == True:
                    board.guess_board[tries] = "p"
                    board.draw_board()
                    tries += 1

                else:
                    continue
                board.board[turn] = board.guess_board
                board.draw_board()

            elif tries == 4:
                board.check(board.guess_board, turn)
                board.draw_help_board()
                board.guess_board = ["o", "o", "o", "o"]
                turn += 1
                board.draw_help_board()
                tries = 0

                if board.blacky == 4:
                    pygame.time.wait(150)
                    end_game(turn, solution, bg_win)
                elif turn == 10:
                    pygame.time.wait(150)
                    end_game(turn, solution, bg_lose)
            else: continue

    pygame.display.update()

#----------------------------------------------------
def help ():
    screen.blit(bg_help, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    main_menu()
            else:
                pygame.display.update()

#----------------------------------------------------
def end_game (turn, solution, background):
    screen.blit(background, (0, 0))

    board = Board()
    board.solution(solution)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    ai_vs_p()
#----------------------------------------------------
run()