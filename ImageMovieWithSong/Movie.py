import math

import random
import shutil
from pathlib import Path

import librosa
from moviepy.editor import *

import cv2
def consistent(fps=15, duration=1, SourceFolder=None, DestinationFolder=None, add_song=True, song_dir=None):
    if SourceFolder is None:
        print('You need to choose a source folder!')
    elif DestinationFolder is None:
        print('You need to choose a destination folder!')
    else:
        files_and_duration = []
        for f in os.listdir(SourceFolder):
            print(f'Adding {f} to the frame list with {duration}seconds as the duration')
            files_and_duration.append((os.path.join(SourceFolder, f), duration))
        w, h = None, None
        for file, dur in files_and_duration:
            print(f'Reading {file}')
            frame = cv2.imread(file)
            if w is None:
                h, w, _ = frame.shape
                fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
                writer = cv2.VideoWriter(os.path.join(DestinationFolder, 'tmp_song$%234.mp4'), fourcc, fps,(w, h))
            for repeat in range((duration * fps)):
                writer.write(frame)
            print(f'Wrote {file} {duration * fps} {"time" if duration * fps == 1 else "times"} (frames)')
        writer.release()
        if add_song == True:
            os.system(f'ffmpeg -i {os.path.join(DestinationFolder, "tmp_song$%234.mp4")} -i {song_dir} -map 0:0 -map 1:0 -c:v copy -c:a copy {os.path.join(Path(__file__).parent.absolute(), "image_sequance_output.mp4")}')
            os.remove(os.path.join(DestinationFolder, 'tmp_song$%234.mp4'))
            shutil.move(os.path.join(Path(__file__).parent.absolute(), 'image_sequance_output.mp4'), DestinationFolder)
            print(f'Adding {os.path.basename(song_dir)} to the video file')
        print(f'Done! File in {DestinationFolder}')
import IPython.display as ipd

song = os.path.join('C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Song', 'song.mp3')

from pydub import AudioSegment


def tempo(fps=15, SourceFolder=None, DestinationFolder=None):
    global song
    if SourceFolder is None:
        print('You need to choose a source folder!')
    elif DestinationFolder is None:
        print('You need to choose a destination folder!')
    else:

        files_path = 'C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Song'
        file_name = 'song'
        startMin = 1
        startSec = 0
        endMin = 2
        endSec = 0
        startTime = startMin * 60 * 1000 + startSec * 1000
        endTime = endMin * 60 * 1000 + endSec * 1000
        song1 = AudioSegment.from_mp3(song)
        extract = song1[startTime:endTime]
        extract.export(os.path.join(files_path, 'time-thing.mp3'), format="mp3")
        song = os.path.join(files_path, 'time-thing.mp3')
        old_song = os.path.join('C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Song', 'song.mp3')
        x, sr = librosa.load(song)
        ipd.Audio(x, rate=sr)
        tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')
        tempo = round(tempo * 2)

        video_duration = librosa.get_duration(filename=song) / 60
        tmp = video_duration % 1
        tmp = tmp * 60
        tmp = math.floor(tmp) * 0.01
        tmp2 = math.modf(video_duration)
        video_duration = tmp2[1] + tmp
        beats = math.floor(tempo * video_duration)
        beats_a_sec = tempo / 60
        print(beats, video_duration, tempo, beats_a_sec)

        files_and_duration = []
        for f in os.listdir(SourceFolder):
            files_and_duration.append((os.path.join(SourceFolder, f), beats_a_sec))
        w, h = None, None
        for file, dur in files_and_duration:
            frame = cv2.imread(file)
            if w is None:
                h, w, _ = frame.shape
                fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
                writer = cv2.VideoWriter(os.path.join(DestinationFolder, 'output.mp4'), fourcc, fps,(w, h))
            for repeat in range(math.floor(beats_a_sec*10)*2 + 1):
                writer.write(frame)
        writer.release()
        os.system(f'ffmpeg -i {os.path.join(DestinationFolder,"output.mp4")} -i {old_song} -map 0:0 -map 1:0 -c:v copy -c:a copy {os.path.join(DestinationFolder,"outputwa.mp4")}')

def random_duration(min_range=1, max_range=2.5, SourceFolder=None, DestinationFolder=None, fps=15):
    if SourceFolder is None:
        print('You need to choose a source folder!')
    elif DestinationFolder is None:
        print('You need to choose a destination folder!')
    else:
        files_and_duration = []
        for f in os.listdir(SourceFolder):
            files_and_duration.append((os.path.join(SourceFolder, f), round(random.uniform(min_range,max_range), 1)))
        w, h = None, None
        for file, dur in files_and_duration:
            frame = cv2.imread(file)
            if w is None:
                h, w, _ = frame.shape
                fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
                writer = cv2.VideoWriter(os.path.join(DestinationFolder, 'output.mp4'), fourcc, fps,(w, h))

            for repeat in range(round(dur * fps)):
                writer.write(frame)
        writer.release()

SourceFolder = 'C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Jpeg'
DestinationFolder = 'C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Dest'

consistent(SourceFolder=SourceFolder, DestinationFolder=DestinationFolder, add_song=True, song_dir='C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Song\\song.mp3')
#random_duration(SourceFolder='C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Jpeg', DestinationFolder='C:\\Users\ilaik\Videos\VideosForPepole\Dad2021BD\Images\Regualr\Dest')
