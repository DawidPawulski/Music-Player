import pygame
from mutagen.mp3 import MP3
import time


paused = False # set a state of songs paused or not paused
song_index = 0  # set idex for playing songs from a list which is later modified 

def print_time(song):	
    song_length = round(MP3(song).info.length)
    for i in range(song_length, 0, -1):
        time.sleep(1)
        current_time = i // 60 + (i % 60 / 100)
        print("{0:.2f}".format(current_time))


def sum_of_song_length(list_of_songs): # count sum length for all songs  
    sum_of_song_length = sum([round(MP3(song).info.length) for song in list_of_songs])  # taking songs length sum
    sum_of_song_length_in_min_sec = sum_of_song_length // 60 + (sum_of_song_length % 60 / 100)  # convert sec into minutes and seconds
    return sum_of_song_length_in_min_sec

def play_song(song):
    global paused
    if paused:
        unpause_song()
    else:   
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True

def unpause_song():
    global paused
    pygame.mixer.music.unpause()
    paused = False

def repeat_song(song):
    PLAY_SONG_INFINITELY = -1
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

def play_playlist(songs, song_index):
    
    song = songs[song_index]
    play_song(song)

def next_song(songs):
    global song_index # set index for a playlist
    song_index += 1
    play_playlist(songs, song_index)

def previous_song(songs):
    global song_index # set index for a playlist
    if song_index >= 1:
        song_index -= 1
        play_playlist(songs, song_index)


def display_playlist(songs):
    result = ""
    for song in songs:
        song_title = song.split("/")
        for song in song_title[-1:]:
            song = song.strip(".mp3")
            result += "{}\n".format(song)
    return result


def shuffle(songs):
    import random
    random.shuffle(songs)
    return songs
