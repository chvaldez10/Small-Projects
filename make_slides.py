"""
    make_slides:    Creates PPT slides with desired format.
                    Default map format: centered, middle, white background, black text, Calibri (body style)
                    Expecting directories to exist: ../Songs/
    ...

    options:
        -s:         Save slides to ../../Songs/

    Usage:          main.py [-options] "Song Title" [num of lines] [refrain]

    Arguments:
        Song Title:                    [Song Title].pptx
        Number of lines per slide:     Maximum number of lines per slide (default 2).
        Chorus/Refrain:                Decides whether to use chorus or refrain as header
"""

import os
import sys
import getopt
import json
from songs import *
from reformat_verse import RevisedSong
from create_slide import MakeSlide

PPT_SONGS_DIR = r"../../Songs"
SONG_LIST_TXT = r"./song_list.txt"


def list_pptx() -> None:
    try:
        pptx_in_folder = os.listdir(PPT_SONGS_DIR)
        txt_path = SONG_LIST_TXT
    except Exception as error:
        print(error)
    else:
        if os.path.exists(txt_path):
            os.remove(txt_path)

        with open(txt_path, "a") as pptx_data:
            [pptx_data.write(f"{pptx}\n") for pptx in pptx_in_folder]


def make_empty_txt_file(filename: str):
    with open(f"{filename}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write("")

    exit(
        f"\nError: Failed to open [{filename}.txt] .. I've created an empty file for next time\n")


def exit(msg=None):
    """Exit the program and print usage message"""
    print(__doc__)

    if msg:
        print(msg)

    sys.exit(0)


def read_json(json_path):
    print("\nReading JSON file\n")
    try:
        with open(f"{json_path}") as sim_json:
            sim_data = json.load(sim_json)
            json_object = json.dumps(sim_data, indent=4)
            print(f"JSON file content: {json_object}\n")

    except Exception as error:
        print(error)
        exit()

    return sim_data


def print_roadmap():
    os.system(r"roadmap.txt")

    try:
        with open("roadmap.txt", "r", encoding="utf-8") as roadmap_data:
            song_roadmap_list = roadmap_data.read().split("\n")
            print("\n    -------------------------\n    |    Current roadmap    |\n    -------------------------\n")
            [print(f"            {roadmap}") for roadmap in song_roadmap_list]
    except Exception as error:
        print(error)
        make_empty_txt_file("roadmap")

    return song_roadmap_list


def read_song_lines(*songs: dict) -> None:
    """
        Reads song objects passed in from a list of songs

        Creates RevidedSong objects where song lyrics are cleaned to pass to MakeSlide class
    """
    for song in songs:
        # unpacking song dictionary
        new_song = RevisedSong(song)
        new_song.read_song()


def get_expected_song_lines() -> list[str]:
    """returns list of expected song lines from template"""
    return list(song_template.keys())

###########################################################
#
#            Main loop for make_slider.py
#
##########################################################


if __name__ == "__main__":
    try:
        expected_song_lines = get_expected_song_lines()
        print(f"Expected verses: {expected_song_lines}")

    except Exception as error:
        print(error)
        exit()

    else:
        # update song_list.txt
        list_pptx()

        # read songs
        read_song_lines(song_template)

        # song1 = RevisedSong(song_verses_list, song_chorus_list, song_bridge_list,
        #                     song_ending_list, num_of_lines, refrain_vs_chorus)
        # song1.create_song_dict()
        # song1_dict = song1.song_dict

        # ppt1 = MakeSlide(song1_dict, song_title, save_slide, song_roadmap_list)
        # ppt1.make_song_slides()
