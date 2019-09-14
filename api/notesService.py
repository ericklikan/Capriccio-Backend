from midiWriter import PITCH, BEATS
from notesRecognizer import X_COORD, Y_COORD
from staffService import get_note_intervals_from_staff_coords

MIDDLE_C_KEY_NUMBER = 40


def convert_coords_to_pitches(staff_coords: list, raw_notes: list) -> list:
    notes = []
    raw_notes.sort(key=lambda x: x.x)
    notes_intervals = get_note_intervals_from_staff_coords(staff_coords)

    for raw_note in raw_notes:
        for i in range(1, len(notes_intervals)):
            if raw_note[Y_COORD] <= notes_intervals[i]:
                notes.append({
                    PITCH: MIDDLE_C_KEY_NUMBER + i,
                    BEATS: 1
                })

    return notes