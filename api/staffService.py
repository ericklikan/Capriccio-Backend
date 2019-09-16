def get_note_intervals_from_staff_coords(staff_coords: list) -> list:
    note_intervals = []
    staff_coords.reverse()

    # print(staff_coords)

    bottom_dist = (staff_coords[0] - staff_coords[1]) / 4
    note_intervals.append(staff_coords[0] + bottom_dist * 3)
    note_intervals.append(staff_coords[0] + bottom_dist * 1)

    for i in range(3):
        temp_dist = (staff_coords[i] - staff_coords[i + 1]) / 4
        note_intervals.append(staff_coords[i] - temp_dist)
        note_intervals.append(staff_coords[i + 1] + temp_dist)

    top_dist = (staff_coords[3] - staff_coords[4]) / 4
    note_intervals.append(staff_coords[4] + top_dist * 1)
    note_intervals.append(staff_coords[4] - top_dist * 1)

    note_intervals.reverse()

    return note_intervals
