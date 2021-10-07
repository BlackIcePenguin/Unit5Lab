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
OCEAN_BLUE = (26, 117, 255)
COLORS = [RED, GREEN, BLUE, WHITE]

# Create Math Constant
PI = math.pi

# To convert from Degrees to Radians -> angle * (pi / 180)

# Game Constants
SIZE = (700, 500)
FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
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
            pygame.draw.arc(screen, BLUE, [self.x + 24 + (0.8 * num), self.y - 40 - (1.2 * num), 15, 50],
                            -PI / 2, PI / 2, 2)
        pygame.draw.line(screen, LIGHT_BROWN, (self.x + 28, self.y - 40), (self.x + 70, self.y - 100), 5)

    def raft_move(self):
        if self.x > 800:
            self.x = -100
        if self.x <= 800:
            self.x += 1.5


class Ocean:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.flow_rate = 5
        self.flow_change = 0.1
        self.flow_x = x

    def flow(self):
        for val in range(-15,  18):
            pygame.draw.ellipse(screen, OCEAN_BLUE, [self.flow_x-(40*val), self.y-5, 60, 20])
        self.flow_x += self.flow_rate
        self.flow_rate -= self.flow_change
        if abs(self.flow_rate) >= 5:
            self.flow_change = -1 * self.flow_change

    def main_ocean(self):
        pygame.draw.rect(screen, OCEAN_BLUE, [0, self.y, SCREEN_WIDTH, SCREEN_HEIGHT])


class Sky:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cloud_shift = 1.5

    def cloud(self):
        for value in range(0, 3):
            pygame.draw.ellipse(screen, WHITE, [self.x + (320 * value), self.y, 100, 30])
            pygame.draw.ellipse(screen, WHITE, [self.x + 30 + (320 * value), self.y - 15, 60, 40])
            pygame.draw.ellipse(screen, WHITE, [self.x + 40 + (320 * value), self.y + 10, 80, 35])
        self.x -= self.cloud_shift
        if self.x <= -160:
            self.x += 320

    @staticmethod
    def sun():
        pygame.draw.circle(screen, YELLOW, (0, 0), 89)


raft = Raft(300, 300)
ocean = Ocean(500, 250)
sky = Sky(300, 100)
while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY_BLUE)
    ocean.main_ocean()
    ocean.flow()
    sky.sun()
    sky.cloud()
    raft.raft_move()
    raft.raft_draw()

    pygame.display.flip()

    clock.tick(FPS)


# Runs when main game loop ends
pygame.quit()
