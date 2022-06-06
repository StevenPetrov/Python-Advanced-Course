def fill_the_box(*args):
    end_index = args.index('Finish')
    small_boxes = list(reversed(args[3:end_index]))
    box_size = args[0] * args[1] * args[2]
    for x in range(len(small_boxes)):
        box_size -= small_boxes.pop()
        if box_size < 0:
            small_boxes.append(abs(box_size))
            break
    if box_size >= 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    return f"No more free space! You have {sum(small_boxes)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
