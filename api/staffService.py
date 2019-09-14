import staffRecognizer


def get_note_intervals_from_staff_coords(staff_coords: list) -> list:
    note_intervals = []
    staff_coords.reverse()

    bottom_dist = (staff_coords[0] - staff_coords[1]) / 4
    note_intervals.append(staff_coords[0] + bottom_dist * 3)
    note_intervals.append(staff_coords[0] + bottom_dist * 1)

    for i in range(3):
        temp_dist = (staff_coords[i] - staff_coords[i + 1]) / 4
        note_intervals.append(staff_coords[i] - temp_dist)
        note_intervals.append(staff_coords[i + 1] + temp_dist)

    top_dist = (staff_coords[3] - staff_coords[4]) / 4
    note_intervals.append(staff_coords[4] - top_dist * 1)
    note_intervals.append(staff_coords[4] - top_dist * 3)

    return note_intervals


# print(staffRecognizer.find_staff_coordinates('../image/69982062_361377188078148_4391311645901586432_n.jpg'))
# staff_coords = staffRecognizer.find_staff_coordinates('../image/69982062_361377188078148_4391311645901586432_n.jpg')
# print(get_note_intervals_from_staff_coords(staff_coords))