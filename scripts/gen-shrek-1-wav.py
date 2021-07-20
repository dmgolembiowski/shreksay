#!/usr/bin/env python3

import extract_audio_wav as eaw
from preprocess_shrek1 import *

s1 = load_only_shrek_from_shrek_1_srt()

s1_lines = [
        str(eaw.Ffmpeg_Command(subtitle=sub, mov_path="Shrek_1.wav")) 
        for sub in s1
]

lines = [line + " &\nwait $!\n" for line in s1_lines]


with open('gen_wav_synchronous.sh', 'a+') as f:
    for line in lines:
        f.write(line)
