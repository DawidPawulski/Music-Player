# First you should install mutagen  / sudo pip3 install mutagen /
from mutagen.mp3 import MP3
import time


def print_time(song):
    song_length = round(MP3(song).info.length)
    for i in range(song_length, 0, -1):
        time.sleep(1)
        current_time = i // 60 + (i % 60 / 100)
        print("{0:.2f}".format(current_time))


print(print_time('/home/taras/Desktop/mp/Machinae-Supremacy-Death-from-Above.mp3'))

list_of_songs = ['bensound-dubstep.mp3', 'bensound-epic.mp3']


def sum_of_song_length(list_of_songs): # count sum length for all songs
    sum_of_song_length = sum([round(MP3(song).info.length) for song in list_of_songs])  # taking songs length sum
    sum_of_song_length_in_min_sec = sum_of_song_length // 60 + (sum_of_song_length % 60 / 100) # convert sec into minutes and seconds
    return sum_of_song_length_in_min_sec


#print(sum_of_song_length(list_of_songs))