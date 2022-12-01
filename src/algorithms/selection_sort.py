# Sorting Algorithm Implementation: Selection Sort
from draw_info import array, arr_clr,\
    CYAN, MAGENTA, WHITE, refill, pygame

def selection_sort(array):

    for cur in range(len(array)):
        min_index = cur
        
        for j in range(cur + 1, len(array)):

            pygame.event.pump()
            
            # Select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
            
            arr_clr[j], arr_clr[cur] = CYAN, MAGENTA
            refill()
            arr_clr[j], arr_clr[cur] = WHITE, WHITE

        # Swapping the elements to sort the array
        array[cur], array[min_index] = array[min_index], array[cur]