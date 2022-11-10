import pygame # For all GUI
import random # To generate random values - creating unsorted lists
import math # To calculate floor of block height - preventing overflow
# Test

# Initialize entire pygame module for usage
pygame.init()

# To access global values
class DrawInformation:

    # Define global values as class attributes
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    CYAN = 0, 255, 255
    MAGENTA = 255, 0, 255
    BACKGROUND_COLOR = BLACK

    GRADIENTS = [
        (145, 145, 0), # Dark Yellow
        (200, 200, 0), # Medium Yellow
        (255, 255, 0) # Light Yellow
    ]

    fontname = 'inkfree'
    fontsize = 30
    FONT = pygame.font.SysFont(fontname, fontsize)
    LARGE_FONT = pygame.font.SysFont(fontname, fontsize*2, bold=pygame.font.Font.bold)

    # Set total fixed padding for left and right side
    SIDE_PAD = 400
    # Set padding between controls and visualization
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        # width will scale with n of lst elements
        self.width = width

        # height will scale with range of lst values
        self.height = height

        # Setup window screen as attribute
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # To represent all the width of all blocks
        total_width = self.width - self.SIDE_PAD
        # Calculate width for each block
        self.block_width = round(total_width / len(lst))
 
        # To represent the height of the blocks
        total_height = self.height - self.TOP_PAD
        # To represent relative height range between blocks: greater the range, shorter the block
        height_range = self.max_val - self.min_val
        # Calculate height for each block
        self.block_height = math.floor(total_height / height_range)

        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, sorting_algo_name, ascending):
    
    caption_top_pad = 20
    
    # Draw every single frame
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{sorting_algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.MAGENTA)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, caption_top_pad))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sort | A - Ascending | D - Descending", 1, draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, caption_top_pad*4))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort | Q - Quick Sort", 1, draw_info.CYAN)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, caption_top_pad*6))
    
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        # How wide to draw each block
        x = draw_info.start_x + i * draw_info.block_width
        # How far down to draw for each block
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        # Ensure every element with have a different grey color
        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        # Plot the rectangle elements
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
        # Plot the separation between rectangle elements
        pygame.draw.rect(draw_info.window, draw_info.BLACK, (x, y, draw_info.block_width/5, draw_info.height))

    if clear_bg:
        pygame.display.update() 

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
                # If numbers are sorted, draw shifted elements
                draw_list(draw_info, {j: draw_info.CYAN, j + 1: draw_info.MAGENTA}, True)
                yield True

    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        cur = lst[i]

        while True:
            # True if last element greater than current element, and set to ascending
            ascending_mode = lst[i - 1] > lst[i] and i > 0 and ascending
            # True if last element less than current element, and set to descending
            descending_mode = lst[i - 1] < lst[i] and i > 0 and not ascending

            # If neither modes are true, then sort is done thus break
            if not ascending_mode and not descending_mode:
                break

            lst[i] = lst[i - 1] # Make current
            i -= 1
            lst[i] = cur
                
            draw_list(draw_info, {i - 1: draw_info.CYAN, i: draw_info.MAGENTA}, True)
            yield True

    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for cur in range(len(lst)):
        min_index = cur
 
        for j in range(cur + 1, len(lst)):
            # Select the minimum element in every iteration
            if (lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending):
                min_index = j
            draw_list(draw_info, {min_index: draw_info.CYAN, j: draw_info.MAGENTA}, True)
            yield True

        # Swapping the elements to sort the lst
        lst[cur], lst[min_index] = lst[min_index], lst[cur]

def main():
    run = True

    # Regulate game loop
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1200, 700, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    # While the game is running
    while run:
        # Set FPS
        clock.tick(30)

        # Draw information
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        # Event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False         
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quicksort
                sorting_algo_name = "Quick Sort"

        
    pygame.quit()


if __name__ == "__main__":
    main()
