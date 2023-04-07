class RevisedSong:
    """
        Class to format verse

        Desired output looks like this:
        {
            Verse 1: ['Jumping up and down, \nJumping up and down, ', 'Jumping up and down, \nShout Hosanna! Hosanna! ']

            Verse 2: ['Here comes Jesus riding on a donkey, \nHosanna! Hosanna! Hosanna to the King! ', 'Wave the branches of the trees before Him, \nHosanna! Hosanna! Hosanna to the King!']

            Chorus 1: ['And He walks with me, and He talks with me,\nAnd He tells me I am His own;', 'And the joy we share as we tarry there,\nNone other has ever known.']

            Bridge: ['Holy, holy, Lord Almighty\nGood and gracious', 'Good and gracious\nHoly, holy, Lord Almighty']

            Ending: []
        }

    """

    def __init__(self, song: dict) -> None:
        self.song = song
        self.song_parameters = self.song.get(
            "song_parameters", "no song parameters")
        self.num_of_lines = self.song["song_parameters"]["num_of_lines"]

        self.cleaned_song = {}

    def read_song(self) -> None:
        song_lines = list(self.song.keys())
        song_title = self.song["song_parameters"]["song_title"]

        print(f"\nProcessing: {song_title}\n")

        for verse in song_lines[1:]:
            # identify whole verse
            song_lines = self.song[verse].split("\n\n")
            song_lines = [line.strip()
                          for line in song_lines if line.strip() != ""]

            # remove white space in each clause and returns number of song lines per slide
            self.remove_white_spaces_in_lines(song_lines, verse)

        # print(self.cleaned_song)
        for verse, lyrics in self.cleaned_song.items():
            print(f"{verse}: {lyrics}\n")

    def remove_white_spaces_in_lines(self, song_lines: list[str], verse: str) -> None:
        """splits lines and removes whitespace"""
        song_lines_tmp = []

        for count, line in enumerate(song_lines):
            new_line = line.split("\n")
            new_line = [line.strip() for line in new_line]

            # revising songs based on number of lines per slide
            song_lines_revised = self.revise_song_lines(new_line)
            self.cleaned_song[f"{verse.title()} {count+1}"] = song_lines_revised

    def revise_song_lines(self, song_lines) -> list[str]:
        song_lines_len = len(song_lines)
        revised_song_lines = []

        for ittr_i in range(0, song_lines_len, self.num_of_lines):
            tmp_str = ""
            tmp_list = []
            [tmp_list.append(song_lines[ittr_j])
             for ittr_j in range(ittr_i, ittr_i+self.num_of_lines) if ittr_j < song_lines_len]

            tmp_str = "\n".join(tmp_list)
            revised_song_lines.append(tmp_str)

        return revised_song_lines
