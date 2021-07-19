#!/usr/bin/env python3
import srt
import pickle
import pathlib
from typing import * # NoQA


def load_shrek_2_srt() -> List[srt.Subtitle]:
    subs: List[srt.Subtitle]

    srt_path = str(pathlib.Path(__file__).parent.parent) + "/data/Shrek_2.srt"
    
    with open(srt_path, "r") as srt_stream:
        content = srt_stream.read()
        subs    = list(srt.parse(content))
        return subs

def load_only_shrek_from_shrek_2_srt() -> List[srt.Subtitle]:
    subtitles = load_shrek_2_srt()
    filtered: List[srt.Subtitle] = list()

    for (idx, sub_slot) in enumerate(subtitles):
        if sub_slot.content.startswith("SHREK\n"):
            try:
                assert "FIONA" not in sub_slot.content
                assert "DONKEY" not in sub_slot.content
                assert "FARQUAAD" not in sub_slot.content
                assert "GINGERBREAD MAN" not in sub_slot.content

                filtered.append(sub_slot)
            except AssertionError:
                continue

    return filtered

subtitles = load_only_shrek_from_shrek_2_srt()

import pprint
pprint.pprint(subtitles)

print(f"Getting {len(subtitles)} distinct training sound bytes for Shrek 2")
