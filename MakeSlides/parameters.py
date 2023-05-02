import collections
import collections.abc
from pptx.util import Cm

TOP_ALIGN = 2.025
LEFT_ALIGN = -2.78
SLIDE_WIDTH = 30.96
SLIDE_HEIGHT = 15

LEFT = Cm(LEFT_ALIGN)
TOP = Cm(TOP_ALIGN)
WIDTH = Cm(SLIDE_WIDTH)
HEIGHT = Cm(SLIDE_HEIGHT)

HEADER_HEIGHT = Cm(1.28)
HEADER_TOP_ALIGN = Cm(0.1)

save_file = False
text_font = "Calibri (Body)"

PPT_FOLDER_PREFIX = "./"
SONGS_DIRECTORY = r"./songs/"
SONG_LIST_TXT = r"song_list.txt"
ROADMAP_TXT_FILE = r"roadmap.txt"