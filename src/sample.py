# For GUI Implementation
from draw_info import *

# Sorting Algorithm Implementation
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.quick_sort import quick_sort


def main():
    sorting = False
    run = True
    while run:

        # Redraw array and prevent stacking
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
                algo_name = "Quick Sort"

            elif event.key == pygame.K_b and not sorting:
                run_sort(sorting, bubble_sort(array))
                algo_name = "Bubble Sort"

            elif event.key == pygame.K_s and not sorting:
                run_sort(sorting, selection_sort(array))
                algo_name = "Selection Sort"

            elif event.key == pygame.K_i and not sorting:
                run_sort(sorting, insertion_sort(array))
                algo_name = "Insertion Sort"

        draw()
        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()