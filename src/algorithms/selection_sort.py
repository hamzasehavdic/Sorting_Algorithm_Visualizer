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