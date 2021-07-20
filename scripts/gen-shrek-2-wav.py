#!/usr/bin/env python3

import extract_audio_wav as eaw
from preprocess_shrek2 import *

s2 = load_only_shrek_from_shrek_2_srt()

s2_lines = [
        str(eaw.Ffmpeg_Command(subtitle=sub, mov_path="Shrek_2.wav")) 
        for sub in s2
]

lines = [line + " &\nwait $!\n" for line in s2_lines]


with open('gen_wav_synchronous.sh', 'a+') as f:
    for line in lines:
        f.write(line)
