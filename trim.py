from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import mimetypes
import time
import os

def to_seconds(timestamp):
    """
    take timestamp hrs:min:sec
    and return the value in second
    """
    hrs,mint,sec=timestamp.split(":")
    hrs2sec = int(hrs)*60*60
    mint2sec = int(mint)*60
    
    return hrs2sec + mint2sec + int(sec)

def trim_video(path,start,end,export_path):
    """
    path --> string :: path of video to trim.
    start --> int (seconds):: start time to trim.
    end --> int (seconds):: end time to trim.
    export_path --> string :: path to save trimmed video
    
    trim video 
    take from `path`
    trim from `start` 2 `end`
    and save to `export_path`
    """
    if mimetypes.guess_type(path)[0].startswith('video'):
        ffmpeg_extract_subclip(path, start, end, targetname=export_path)
        return True
    else:
        raise TypeError("not a video")

if __name__ == "__main__":
    start_time = input("enter start time in form HH:MM:SS")
    end_time = input("enter end time in form HH:MM:SS")

    start_time = to_seconds(start_time)
    end_time = to_seconds(end_time)

    path = input("enter end path of video")
    export_path = input("enter end path to export trimmed video")

    try:
        trim_video(path,start_time,end_time,export_path)
    except Exception as e:
        print(e)