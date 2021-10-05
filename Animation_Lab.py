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
day_night = 0
am = True
tree_shift = 400
norm_shift = 0
orb_shift = 0
theta = 0


# Setting the sky loop color
def sky_color(time):
    sky_color_a = (0, 190 * time / 900, 255 * time / 900)
    return sky_color_a


# Tree, based on bottom right point on tree for x
def tree_builder(x, y, tree_change):
    pygame.draw.rect(screen, BROWN, [x-20, y-80, 20, 80], width=0)
    for number in range(0, 2):
        pygame.draw.polygon(screen, DARK_GREEN, [(x-60, tree_shift-60-60*number), (x+40, tree_shift-60-60*number),
                                                 (x-10, tree_shift-180-(60*number))], width=0)


# Human code, bottom right foot starting x and y
def waving_person(x, y, time):
    pygame.draw.line(screen, MAGENTA, (x, y), (x+10, y-30), width=4)
    pygame.draw.line(screen, MAGENTA, (x + 20, y), (x + 10, y - 30), width=4)
    pygame.draw.line(screen, MAGENTA, (x + 10, y - 30), (x + 10, y - 60), width=4)
    pygame.draw.circle(screen, MAGENTA, (x + 11, y-60), 10, 0)
    pygame.draw.line(screen, MAGENTA, (x + 10, y - 35), (x + 35, y-70), width=4)
    pygame.draw.line(screen, MAGENTA, (x + 35, y - 70), (x + 25 + time, y-90), width=4)


running = True

while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False

    # Game logic (Objects fired, object movement) goes here

    # Setting the sky and its change, full loop every 30 seconds
    screen.fill(sky_color(day_night))
    if day_night == 900:
        day_night -= 1
        am = False
    elif day_night == 0 and am is False:
        am = True
        day_night += 1
    elif day_night < 900 and am is True:
        day_night += 1
    elif day_night < 900 and am is False:
        day_night -= 1

    # Trees moving via sky cycle
    if am is True:
        tree_shift += 1/36
        norm_shift += 1/18
    elif am is False:
        tree_shift -= 1/36
        norm_shift -= 1/18
    theta += math.pi/24
    # Add drawings here
    pygame.draw.rect(screen, GREEN, [0, 400, 700, 500], width=0)
    if orb_shift < 800:
        orb_shift += 2
        pygame.draw.circle(screen, YELLOW, [-50 + orb_shift, 70], 25, width=0)
    for num in range(0, 4):
        pygame.draw.ellipse(screen, WHITE, [(80 + 180*num) + norm_shift, 100 - 10*num, 120, 60], width=0)
    for val in range(0, 6):
        tree_builder(70 + 115*val, 400, tree_shift)
    hoop_x = int(200 + 50*math.cos(theta))
    hoop_y = int(100 + 50*math.sin(theta))
    pygame.draw.circle(screen, RED, (hoop_x, hoop_y), 10, 0)
    wave_time = day_night / 45
    waving_person(300, 400, wave_time)

    pygame.display.flip()

    clock.tick(FPS)


# Runs when main game loop ends
pygame.quit()
