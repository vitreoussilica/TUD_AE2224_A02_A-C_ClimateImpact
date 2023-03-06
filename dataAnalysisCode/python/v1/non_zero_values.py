def find_non_zero_values(array):
    i_x = 0
    i_y = 0
    i_z = 0
    i_w = 0
    non_zero_values = []
    non_zero_indices = []
    for x in array:
        i_y = 0
        i_z = 0
        i_w = 0
        for y in x:
            i_z = 0
            i_w = 0
            for z in y:
                i_w = 0
                for w in z:
                    if w > 0 or w < 0:
                        non_zero_values.append(w)
                        non_zero_indices.append([i_x, i_y, i_z, i_w])
                    i_w += 1
                i_z += 1
            i_y += 1
        i_x += 1
    return non_zero_values, non_zero_indices