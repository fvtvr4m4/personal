# download youtube playlist and convert to mp3 for custom spotify lib

# pytube allos us to easily download youtube videos or playlists
# msince pytube downloads youtube videos as mp4 we need moviepy to convert
# to mp3 (spotify allows mp4 but mp3 files are lighter)

from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

# grab your playlist from youtube and create a playlist obj
playlist = Playlist("https://www.youtube.com/playlist?list=PLoO9vxMkmtm3gyZf7y7wVwAhWHd6-xdAG")



# # prints each video url, which is the same as iterating through playlis.video_urls
# for url in playlist:
#     print(url)
#
# # prints address of each youtube object in the playlists
# for vid in playlist.videos:
#     print(vid)



# converts url into a YouTube obj, gets the streams, filters to only audio file
# types, then downloads the first stream listed
# for url in playlist:
#     YouTube(url).streams.filter(only_audio=True).first().download()

# downloads first stream for each video to chosen folder
for url in playlist:
    YouTube(url).streams.first().download("/Users/mariliasampaio/youtube songs")

# convert each mp4 to mp3 and delete original mp4 copy

# get path for folder
folder = "/Users/mariliasampaio/youtube songs"

for file in os.listdir(folder):
    # if file we are looking at is indeed an mp4 file...
    if re.search("mp4", file):
        # gives us path to the file we are looking at in the specific iteration
        # by joining the folder path with the file name
        mp4_path = os.path.join(folder, file)
        # give us path to a file with the same name as the mp4 file but now with
        # an mp3 extention
        mp3_path = os.path.join(folder, os.path.splitext(file)[0]+".mp3")
        # create new mp3 file by using the AudioFileClip func form moviepy
        new_file = mp.AudioFileClip(mp4_path)
        # write this file to the path create by our initialization of the mp3 path
        # so we have now created the mp3 file in that same folder
        new_file.write_audiofile(mp3_path)
        # delete mo4s
        os.remove(mp4_path)

# the folder should now have mp3 on it
# go to spotify settings and enable local files and select folder
# to access via phone: computer and phone must be on same network
# local files on the playlist will download to your phone
