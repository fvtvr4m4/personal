# Downloads youtube playlist and converts to mp3 for custom spotify playlist

# Libraries used:
# Pytube - allows easy download of youtube videos or playlists
# Moviepy - converts mp4 files to mp3 (spotify allows mp4, but mp3 files are lighter)

from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp

def main():
    # Grabs playlist from youtube and create a playlist obj
    playlist = Playlist("https://www.youtube.com/playlist?list=PLoO9vxMkmtm3gyZf7y7wVwAhWHd6-xdAG")

    # Prints each video url, which is the same as iterating through playlist.video_urls
    # for url in playlist:
    #     print(url)
    #
    # Prints address of each youtube object in the playlists
    # for vid in playlist.videos:
    #     print(vid)
    #
    # Converts url into a YouTube obj, gets the streams, filters to only audio file
    # types, then downloads the first stream listed
    # for url in playlist:
    #     YouTube(url).streams.filter(only_audio=True).first().download()

    # Downloads first stream for each video to chosen folder
    for url in playlist:
        YouTube(url).streams.first().download("/Users/mariliasampaio/youtube songs")

    # Converts each mp4 to mp3 and deletes original mp4 copy
    # Get path for folder
    folder = "/Users/mariliasampaio/youtube songs"

    for file in os.listdir(folder):
        # If file we are looking at is indeed an mp4 file...
        if re.search("mp4", file):
            # Gives us path to the file we are looking at in the specific iteration
            # by joining the folder path with the file name
            mp4_path = os.path.join(folder, file)
            # Give us path to a file with the same name as the mp4 file but now with
            # an mp3 extention
            mp3_path = os.path.join(folder, os.path.splitext(file)[0]+".mp3")
            # Create new mp3 file by using the AudioFileClip func from moviepy
            new_file = mp.AudioFileClip(mp4_path)
            # Write this file to the path created by our initialization of the mp3 path
            # so we have now created the mp3 file in that same folder
            new_file.write_audiofile(mp3_path)
            # Delete mp4s
            os.remove(mp4_path)
main()

    # The folder should now have mp3 files in it
    # Go to spotify settings and enable local files and select folder
    # To access via phone: computer and phone must be on same network
    # local files in the playlist will download to your phone
