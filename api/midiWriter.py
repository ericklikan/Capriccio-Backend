import os
from midiutil import MIDIFile
from flask import current_app as app

BEATS = "beats"
PITCH = "pitch"


class MidiWriter:
    def __init__(self):
        return

    def add_track(self, notes: list, id: str):
        track = 0
        channel = 0
        time = 0
        duration = 1
        tempo = 160
        volume = 100

        COUNT = 0

        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)

        for note in notes:
            COUNT = (COUNT + 1) % 7
            MyMIDI.addNote(track, channel, note[PITCH], time, duration, volume)
            time += note[BEATS]
            if COUNT % 7 == 0:
                time += 1

        with open(os.path.join(app.root_path, app.config["UPLOAD_FOLDER"], "{}.mid".format(id)), "wb") as output_file:
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
