# For GUI
import pygame

# Create unsorted lists using random values
import random

# To calculate floor of block height - preventing overflow
import math
import os
import psutil


pygame.init()

# Window size
width = 1200
length = 700

# Display dimensions
screen = pygame.display.set_mode((width, length))

# Padding
SIDE_PAD = 400
TOP_PAD = 150

# Setup array element data structure: values, colors
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Array for element values
n = 50
array = [0] * n
arr_clr =[(0, 0, 0)] * n

# Generate array elements values and colour
def generate_arr():
    for i in range(1, n):
        arr_clr[i] = WHITE
        array[i] = random.randrange(1, 100)

generate_arr()


# Width for elements within screen
total_width = width - SIDE_PAD
block_width = round(total_width / len(array))

# Length for elements within screen
total_length = length - TOP_PAD
length_range = max(array) - min(array) # Relative range between block lengths
block_length = math.floor(total_length / length_range)

# Font details
fontname = "Tahoma"
LARGE_FONT = pygame.font.SysFont(fontname, 40, bold=pygame.font.Font.bold)
FONT = pygame.font.SysFont(fontname, 25)


def mem_use():
    # Check performance
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
    print('memory use:', memoryUse)


def draw():
    top_padding = 20
    start_x = SIDE_PAD // 2

    # Render Title, then position on screen
    title = LARGE_FONT.render(f"Select Sorting Algorithm", 1, WHITE)
    screen.blit(title, (width/2 - title.get_width()/2, top_padding))

    # Render Reset text, then position on screen
    reset_txt = FONT.render("R = Reset", 1, CYAN)
    screen.blit(reset_txt, (width/2 - reset_txt.get_width()/2, top_padding * 4))

    # Render Algorithm name, then position on screen
    algo_txt = FONT.render("i = Insertion Sort | b = Bubble Sort | s = Selection Sort | q = Quick Sort", 1, MAGENTA)
    screen.blit(algo_txt, (width/2 - algo_txt.get_width()/2, top_padding * 6))

    # Drawing each block on screen
    for i, val in enumerate(array):

        # Check performance
        mem_use()

        # Block width
        x = start_x + i * block_width
        # Block length: how far down to draw length
        y = length - (val - min(array)) * block_length

        # Draw each block as white rect, draw ontop each block a black rect for separation
        pygame.draw.rect(screen, arr_clr[i], (x, y, block_width, length))
        pygame.draw.rect(screen, BLACK, (x, y, block_width/5, length))


def refill():
    screen.fill(BLACK) # Fill display WHITE background colour
    draw()
    pygame.display.update() # Update the display
    pygame.time.delay(60) # Ensure 30fps


def run_sort(sorting, sorting_algorithm):
    sorting = True
    sorting_algorithm
    sorting = False
