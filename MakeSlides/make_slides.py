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
from parameters import *
from songs import *
from reformat_verse import RevisedSong
from create_slide import MakeSlide

"""Move list_pptx and read_json functions to CreateSlide class"""

def list_pptx() -> None:
    try:
        pptx_in_folder = os.listdir(SONGS_DIRECTORY)
        txt_path = SONG_LIST_TXT
    except Exception as error:
        print(error)
    else:
        if os.path.exists(txt_path):
            os.remove(txt_path)

        with open(txt_path, "a") as pptx_data:
            [pptx_data.write(f"{pptx}\n") for pptx in pptx_in_folder]


def read_json():
    print("\nReading JSON file\n")
    try:
        with open("parameters.json") as param_data:
            params = json.load(param_data)
            json_object = json.dumps(params, indent=4)
            print(f"JSON file content: {json_object}\n")

    except Exception as error:
        print(error)
        exit()


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


def read_song_lines(*songs: dict) -> None:
    """
        Reads song objects passed in from a list of songs

        Creates RevidedSong objects where song lyrics are cleaned to pass to MakeSlide class
    """
    for song in songs:
        # unpacking song dictionary
        new_song = RevisedSong(song)
        new_song.read_song()

        song_dict = new_song.cleaned_song
        song_roadmap = new_song.roadmap
        song_title = new_song.song_title

        verify_roadmap(song_roadmap)
        new_ppt = MakeSlide(song_dict, song_title, save_file, song_roadmap)
        new_ppt.make_song_slides()

def verify_roadmap(song_roadmap: list[str]) -> None:
    print_hamburger("Roadmap", song_roadmap)
    with open(ROADMAP_TXT_FILE, "w") as roadmap_file:
        [roadmap_file.write(f"{roadmap}\n") for roadmap in song_roadmap]
    
    os.system(ROADMAP_TXT_FILE)


def get_expected_song_lines() -> list[str]:
    """returns list of expected song lines from template"""
    return list(song_template.keys())


def print_hamburger(header: str, list_of_ingredients: list[str]) -> None:
    """Prints out hamburger text given a list of strings and header"""
    header_len = len(header)
    padding = header_len + 2*10

    # adding | symbol adds a space
    padding_for_header = padding-2

    hdr = header.center(padding_for_header, " ")
    print("\t", "-"*padding)
    print("\t|", hdr, "|")
    print("\t", "-"*padding)

    for ingredient in list_of_ingredients:
        ingr = ingredient.center(padding, " ")
        print("\t", ingr)

###########################################################
#
#            Main loop for make_slider.py
#
##########################################################


if __name__ == "__main__":
    try:
        expected_song_lines = get_expected_song_lines()
        print_hamburger("Expected Song Lines", expected_song_lines)

    except Exception as error:
        print(error)
        exit()

    else:
        # read songs
        read_song_lines(song_template)

        # song1 = RevisedSong(song_verses_list, song_chorus_list, song_bridge_list,
        #                     song_ending_list, num_of_lines, refrain_vs_chorus)
        # song1.create_song_dict()
        # song1_dict = song1.song_dict

        # ppt1 = MakeSlide(song1_dict, song_title, save_slide, song_roadmap_list)
        # ppt1.make_song_slides()
