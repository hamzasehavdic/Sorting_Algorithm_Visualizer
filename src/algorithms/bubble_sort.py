# Sorting Algorithm Implementation: Bubble Sort
from draw_info import array, arr_clr,\
    CYAN, MAGENTA, WHITE, refill, pygame

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):

            pygame.event.pump()
            
            if array[j] > array[j + 1]: 
                array[j], array[j + 1] = array[j + 1], array[j]
            
            arr_clr[j], arr_clr[j + 1] = CYAN, MAGENTA
            refill()
            
            arr_clr[j], arr_clr[j + 1] = WHITE, WHITE