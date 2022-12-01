# Sorting Algorithm Implementation: Quick Sort
from draw_info import array, arr_clr,\
    CYAN, MAGENTA, WHITE, refill, pygame

def quick_sort(array, l, r):
	if l<r:
		pi = partition(array, l, r)
		quick_sort(array, l, pi-1)
		refill()

		quick_sort(array, pi + 1, r)
		
# Function to partition the array
def partition(array, low, high):
	pygame.event.pump()
	pivot = array[high]
	arr_clr[high]= CYAN
	i = low-1
	for j in range(low, high):
		arr_clr[j]= MAGENTA
		refill()
		arr_clr[high]= CYAN
		arr_clr[j]= WHITE
		arr_clr[i]= WHITE
		if array[j]<pivot:
			i = i + 1
			arr_clr[i]= MAGENTA
			array[i], array[j]= array[j], array[i]
	refill()
	arr_clr[i]= WHITE
	arr_clr[high]= WHITE
	array[i + 1], array[high] = array[high], array[i + 1]
	
	return (i + 1)