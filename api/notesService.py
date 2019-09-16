from .midiWriter import PITCH, BEATS
from .notesRecognizer import X_COORD, Y_COORD
from .staffService import get_note_intervals_from_staff_coords

NOTE_PITCHES_DICT = [40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61]


def convert_coords_to_pitches(staff_coords: list, raw_notes: list) -> list:
    notes = []
    raw_notes.sort(key=lambda x: x[X_COORD])
    notes_intervals = get_note_intervals_from_staff_coords(staff_coords)

    notes_intervals.reverse()

    # print("notes_intervals")
    # print(notes_intervals)

    for raw_note in raw_notes:
        for i in range(0, len(notes_intervals)):
            if raw_note[Y_COORD] >= notes_intervals[i]:
                notes.append({
                    PITCH: NOTE_PITCHES_DICT[i],
                    BEATS: 1
                })
                break

    return notes
