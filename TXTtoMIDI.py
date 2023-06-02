from tkinter import *
from tkinter import filedialog
from midiutil.MidiFile import MIDIFile
from math import ceil


def split_txt(filename):

    f = open(filename, "r")

    track = []

    for line in f:
        if line and line != "\n":
            note = []
            for word in line.split():
                note.append(word)
            track.append(note)

    return track


def seconds_to_beats(seconds):
    return ceil(2*seconds)


def assemble_midi(txt_track):

    mf = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)

    for note in txt_track:
        pitch, volume, duration = note
        pitch = int(pitch)
        volume = int(volume)
        beats = seconds_to_beats(float(duration))
        mf.addNote(track, channel, pitch, time, beats, volume)
        time += beats + 1

    return mf


def browse_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename()


def browse_output_file():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename(defaultextension=".mid")


def generate_midi(file):
    track = split_txt(file)
    mf = assemble_midi(track)
    browse_output_file()
    with open(output_file_path, 'wb') as out:
        mf.writeFile(out)