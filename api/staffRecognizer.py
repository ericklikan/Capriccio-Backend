from PIL import Image
from .notesRecognizer import GripPipeline
from .notesService import convert_coords_to_pitches
from .midiWriter import MidiWriter
from .staffService import get_note_intervals_from_staff_coords

RGB_BLACK = (0, 0, 0)
RGB_DIFFERENCE = 100

PIXEL_DIFFERENCE = 10


def is_rgb_value_similar(value1, value2):
    if (abs(value1[0] - value2[0]) <= RGB_DIFFERENCE and
        abs(value1[1] - value2[1]) <= RGB_DIFFERENCE and
        abs(value1[2] - value2[2]) <= RGB_DIFFERENCE):
        return True
    return False


def find_staff_coordinates(image :str) -> list:
    im = Image.open(image)
    pix = im.load()
    x, y = im.size
    mid = x - 100

    line_count = 0
    staff_coordinates = []

    for i in range(y):

        # print(str(i) + " " + str(pix[mid,i]))
        if is_rgb_value_similar(pix[mid, i], RGB_BLACK):
            y_coord = i
            if line_count == 0 or abs(y_coord - staff_coordinates[line_count - 1]) > PIXEL_DIFFERENCE:
                staff_coordinates.append(y_coord)
                line_count += 1

    return staff_coordinates


def generateMidiFileFromImage(id: str, filepath: str):
    staff_coords = find_staff_coordinates(filepath)
    print(staff_coords)
    print("output")
    gripPipeline = GripPipeline()
    gripPipeline.process(filepath)
    print("notes coordinates")
    gripPipeline.notes_coords.sort(key=lambda x: x['x_coord'])
    print(gripPipeline.notes_coords)
    print("notes pitches")
    note_pitches = convert_coords_to_pitches(staff_coords, gripPipeline.notes_coords)
    print(note_pitches)
    midiWriter = MidiWriter()
    midi_notes = midiWriter.convert_note_pitches_to_midi(note_pitches)
    midiWriter.add_track(midi_notes, id)
