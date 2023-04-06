from levenshtein_ratio_and_distance_function import levenshtein_ratio_and_distance
import numpy as np

class CheckSongName:
    def __init__(self, song_name):
        self.song_name = song_name
        self.song_name_list = []
        self.end_check = False

        self.format_name_list()
        self.check_name()

    def format_name_list(self):
        try:
            with open("song_list.txt", "r") as song_data:
                song_names = song_data.read().split("\n")
        except FileNotFoundError as error:
            print(error)
        else:
            for name in song_names:
                temp = name.replace('.pptx', '')
                new_temp = temp.encode("ascii", "ignore")
                new_temp = new_temp.decode()

                self.song_name_list.append(new_temp)

            if '' in self.song_name_list:
                self.song_name_list.remove('')

            # print(self.song_name_list)
            # print(len(self.song_name_list))

    def check_name(self):
        # print(self.song_name)
        # a = "jkhk"
        # print(type(a))
        for song in self.song_name_list:
            song_name_distance = levenshtein_ratio_and_distance(self.song_name, song)
            song_name_ratio = levenshtein_ratio_and_distance(self.song_name, song, ratio_calc=True)

            if np.float64(song_name_ratio).item() > 0.8:
                print(f"\nWe've got a match for user input: {self.song_name}\n")
                print(song_name_distance, song_name_ratio)
                
                if input('Do you want to continue?: ') == 'No'.title():
                    print("exiting")
                    self.end_check = True
                break

        # Distance = levenshtein_ratio_and_distance(Str1, Str2)
        # print(Distance)
        # Ratio = levenshtein_ratio_and_distance(Str1, Str2, ratio_calc=True)
        # print(Ratio)
