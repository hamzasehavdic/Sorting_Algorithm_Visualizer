# Sorting Algorithm Implenetion: Insertion Sort
from draw_info import array, arr_clr,\
    CYAN, MAGENTA, WHITE, refill, pygame

def insertion_sort(array):
    for i in range(1, len(array)):
        cur = array[i]

        
        while True:
            
            pygame.event.pump()
            
            # Draw sort
            arr_clr[i - 1], arr_clr[i] = CYAN, MAGENTA 
            refill()
                
            arr_clr[i - 1], arr_clr[i] = WHITE, WHITE

            # Check for conditions to sort in ascending order
            ascending = array[i - 1] > array[i] and i > 0

            # If neither conditions are true, then break sort
            if not ascending:
                break

            # Since ascending condition satisfied, perform insertion sort
            array[i] = array[i - 1]
            i -= 1
            array[i] = cur
                

    return array