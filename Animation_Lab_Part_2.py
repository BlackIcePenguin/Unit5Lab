import pygame
import math
import random

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (11, 46, 2)
BROWN = (41, 21, 2)
YELLOW = (239, 184, 16)
MAGENTA = (204, 0, 153)
LIGHT_BROWN = (153, 102, 34)
SKY_BLUE = (179, 255, 255)
COLORS = [RED, GREEN, BLUE, WHITE]

# Create Math Constant
PI = math.pi

# To convert from Degrees to Radians -> angle * (pi / 180)

# Game Constants
SIZE = (700, 500)
FPS = 60

# --------------------------------------------------------------------------- #
pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Pygame Lab')

clock = pygame.time.Clock()

running = True


# Setting up the classes
class Raft:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def raft_draw(self):
        pygame.draw.rect(screen, BROWN, [self.x, self.y, 100, 72])
        pygame.draw.line(screen, LIGHT_BROWN, (self.x, self.y + 22), (self.x + 99, self.y + 22), 2)
        pygame.draw.line(screen, LIGHT_BROWN, (self.x, self.y + 48), (self.x + 99, self.y + 48), 2)
        pygame.draw.line(screen, LIGHT_BROWN, (self.x + 50, self.y + 36), (self.x + 50, self.y - 72), 5)
        pygame.draw.line(screen, LIGHT_BROWN, (self.x + 28, self.y + 10), (self.x + 70, self.y - 52), 5)
        pygame.draw.arc(screen, BLUE, [self.x + 24, self.y - 40, 15, 50], -PI/2, PI/2, 2)
        # pygame.draw.arc(screen, BLUE, [self.x + 64, self.y - 100, 15, 50], -PI / 2, PI / 2, 2)
        for num in range(0, 50):
            pygame.draw.arc(screen, BLUE, [self.x + 24 + (0.8 * num), self.y - 40 - (1.2 * num), 15, 50], -PI / 2, PI / 2, 2)
        pygame.draw.line(screen, LIGHT_BROWN, (self.x + 28, self.y - 40), (self.x + 70, self.y - 100), 5)

    def raft_move(self):
        if self.x > 800:
            self.x = -100
        if self.x <= 800:
            self.x += 1.5


class Ocean():
    def __init__(self, x, y):
        self.x = x
        self.y = y


raft = Raft(300, 300)
while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY_BLUE)
    raft.raft_move()
    raft.raft_draw()

    pygame.display.flip()

    clock.tick(FPS)


# Runs when main game loop ends
pygame.quit()
