# For GUI Implementation
from draw_info import *

# Sorting Algorithm Implementation
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.quick_sort import quick_sort

sorting = False
run = True
while run:
    # background
    screen.fill(BLACK)

    # Event handler stores all event
    for event in pygame.event.get():
        
        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False

        if event.type != pygame.KEYDOWN:
            continue

        if event.key == pygame.K_r:
            generate_arr()
        elif event.key == pygame.K_q and not sorting:
            run_sort(sorting, quick_sort(array, 1, len(array)-1))
        elif event.key == pygame.K_b and not sorting:
            run_sort(sorting, bubble_sort(array))

    draw()
    pygame.display.update()
	
pygame.quit()