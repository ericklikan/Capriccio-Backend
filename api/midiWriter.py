from midiutil import MIDIFile

BEATS = "beats"
PITCH = "pitch"
MIDI_FILE_URI = "../midi/test.mid"


class MidiWriter:
    def __init__(self):
        return

    def add_track(self, notes: list):
        track = 0
        channel = 0
        time = 0
        duration = 1
        tempo = 100
        volume = 100

        COUNT = 0

        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)

        for i, note in enumerate(notes):
            COUNT = (COUNT + 1) % 7
            MyMIDI.addNote(track, channel, note[PITCH], time, duration, volume)
            time += note[BEATS]
            if COUNT % 7 == 0:
                time += 1

        with open(MIDI_FILE_URI, "wb") as output_file:
            MyMIDI.writeFile(output_file)


    @staticmethod
    def convert_note_pitches_to_midi(raw_notes: list):
        notes = []
        for raw_note in raw_notes:
            notes.append({
                BEATS: 1,
                PITCH: raw_note[PITCH] + 20
            })

        return notes
