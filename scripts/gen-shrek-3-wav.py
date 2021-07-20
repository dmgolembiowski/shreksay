#!/usr/bin/env python3

import extract_audio_wav as eaw
from preprocess_shrek3 import *

s3 = load_only_shrek_from_shrek_3_srt()

s3_lines = [
        str(eaw.Ffmpeg_Command(subtitle=sub, mov_path="Shrek_3.wav")) 
        for sub in s3
]

lines = [line + " &\nwait $!\n" for line in s3_lines]


with open('gen_wav_synchronous.sh', 'a+') as f:
    for line in lines:
        f.write(line)
