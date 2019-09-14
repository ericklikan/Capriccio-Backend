from midiutil import MIDIFile

BEATS = "beats"
PITCH = "pitch"
MIDI_FILE_URI = "../midi/test.mid"


class MidiWriter:
    def __init__(self):
        return

    def __convert_note_names_to_midi(self, raw_notes: list):
        notes = []
        for raw_note in raw_notes:
            notes.append({
                BEATS: 1,
                PITCH: raw_note[PITCH] + 20
            })

        return notes

    def add_track(self, notes: list):
        track = 0
        channel = 0
        time = 0
        duration = 1
        tempo = 60
        volume = 100

        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)

        for i, note in enumerate(notes):
            MyMIDI.addNote(track, channel, note[PITCH], time, duration, volume)
            time += note[BEATS]

        with open(MIDI_FILE_URI, "wb") as output_file:
            MyMIDI.writeFile(output_file)
