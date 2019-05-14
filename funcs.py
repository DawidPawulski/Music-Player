import pygame
from mutagen.mp3 import MP3
import time


# First you should install mutagen  / sudo pip3 install mutagen /
def print_time(song):
    song_length = round(MP3(song).info.length)
    for i in range(song_length, 0, -1):
        time.sleep(1)
        current_time = i // 60 + (i % 60 / 100)
        print("{0:.2f}".format(current_time))


def sum_of_song_length(list_of_songs):  # count sum length for all songs
    sum_of_song_length = sum([round(MP3(song).info.length) for song in list_of_songs])  # taking songs length sum
    sum_of_song_length_in_min_sec = sum_of_song_length // 60 + (sum_of_song_length % 60 / 100)  # convert sec into minutes and seconds
    return sum_of_song_length_in_min_sec


def init_and_load_song(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)


def play_song(song):
    PLAY_SONG_ONCE = 0
    init_and_load_song(song)
    pygame.mixer.music.play(PLAY_SONG_ONCE)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def stop_song():
    pygame.mixer.music.stop()


def pause_song():
    pygame.mixer.music.pause()


def unpause_song():
    pygame.mixer.music.unpause()


def rewind_song():
    pygame.mixer.music.rewind()


def repeat_song(song):
    PLAY_SONG_INFINITELY = -1
    init_and_load_song(song)
    pygame.mixer.music.play(PLAY_SONG_INFINITELY)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)
    # Set the volume of the music playback. The value argument is between 0.0 and 1.0. When new music is loaded the volume is reset.


def get_songs_from_dir(directory):
    import os
    songs = []
    if '.mp3' in directory:
        songs.append(directory)
    else:
        # r=root, d=directories, f = files
        for r, d, f in os.walk(directory):
            for file in f:
                if '.mp3' in file:
                    songs.append(os.path.join(r, file))
    return songs


def play_playlist(songs):
    for i in range(len(songs)):
        play_song(songs[i])
        '''
        if event = next song
            stop song
            i += 1
        elif event = previous song
            stop song
            i -= 1 or 2 -> needs testing
        '''

def shuffle(songs):
    import random
    random.shuffle(songs)
    print(songs)
    return songs


# print(get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/'))
# play_song(get_songs_from_dir('/home/jck//Documents/python/dizzydeer/DizzyDeer/songs')[0])


play_playlist(shuffle(get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/')))

play_playlist(get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/'))
