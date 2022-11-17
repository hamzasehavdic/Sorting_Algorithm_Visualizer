# Bubble Sort Implementation

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