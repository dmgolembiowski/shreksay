#!/usr/bin/env python3
import urllib.parse as up
import datetime as dt
from typing import Optional

class Ffmpeg_Command:
    
    """Command is a specialized `srt.Subtitles` wrapper type
    
    It's used for "converting" from a Subtitles instance into
    a BASH command statement using ffmpeg.
    """
    def __init__(self, subtitle, mov_path, output_dest=None):
        
        self.subtitle = subtitle
        self.mov_path = mov_path
        self.__output_dest = output_dest

    def __str__(self):

        from_    = '0' + str(dt.timedelta(seconds=self.subtitle.start.seconds))
        from_ext = str(self.subtitle.start.microseconds)[0:3]

        to     = '0' + str(dt.timedelta(seconds=self.subtitle.end.seconds))
        to_ext = str(self.subtitle.end.microseconds)[0:3]

        try:
            try:
                self.output_destination
            except ValueError as e:
                raise(e)
        except AssertionError as e:
            raise(e)

        dest = self.output_destination

        return f'ffmpeg -i {self.mov_path} -ss {from_}.{from_ext} -t {to}.{to_ext} -c copy "{dest}"'

    @property
    def output_destination(self):

        prefix: Optional[str] = None
        
        if self.__output_dest is not None:
            return self.__output_dest
        else:
            if self.mov_path.find('Shrek_1') != -1:
                prefix = "s1_"
            elif self.mov_path.find('Shrek_2') != -1:
                prefix = "s2_"
            elif self.mov_path.find('Shrek_3') != -1:
                prefix = "s3_"
            else:
                raise ValueError("Could not determine proper tagging mechanism on `self.output_destination`")

        assert prefix is not None, "Sanity Check - Unreachable"

        filename_base = self.subtitle.content.lstrip("SHREK\n")
        filename_base = up.quote_plus(filename_base)
        
        if '.' in filename_base:
            filename_base = filename_base.replace('.', '%2E')

        dest = prefix + filename_base + ".wav"
        
        return dest

class Tts_Command:
    
    def __init__(self, text, output_dest: Optional[str] = None):
        self.text = text.replace("SHREK\n", '')
        self.text = self.text.replace("\n", ' ')
        self.__output_dest = output_dset

    @property
    def output_dest(self):
        if self.__output_dest is not None:
            return self.__output_dest
        else:
            dest = self.text.replace(' ', '_')
            dest += '.wav'
            return dest

    def __str__(self):
        return f"mimic -t {self.text} -o {self.output_dest}"
