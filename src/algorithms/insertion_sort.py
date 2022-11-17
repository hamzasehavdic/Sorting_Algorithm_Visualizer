# Insertion Sort Implementation

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