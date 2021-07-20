#!/usr/bin/env python3

import datetime as dt

class Command:
    
    """Command is a specialized `srt.Subtitles` wrapper type
    
    It's used for "converting" from a Subtitles instance into
    a BASH command statement using ffmpeg.
    """
    def __init__(self, subtitle, mov_path, output_dest):
        
        self.subtitle = subtitle
        self.mov_path = mov_path
        self.output_dest = output_dest

    def __str__(self):
        
        from_    = '0' + str(dt.timedelta(seconds=self.subtitle.start.seconds))
        from_ext = str(self.subtitle.start.microseconds)[0:2]
        
        to     = '0' + str(dt.timedelta(seconds=self.subtitle.end.seconds))
        to_ext = str(self.subtitle.end.microseconds)[0:2]
        
        return f"ffmpeg -i {self.mov_path} -ss {from_}.{from_ext} -t {to}.{to_ext} -c copy {self.output_dest}"


