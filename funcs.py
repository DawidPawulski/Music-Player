import pygame
import time


def init_and_load_song(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)


def play_song(song):
    PLAY_SONG_ONCE = 0
    init_and_load_song(song)
    pygame.mixer.music.play(PLAY_SONG_ONCE)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def stop_song(song):
    pygame.mixer.init()
    pygame.mixer.music.stop()


def pause_song(song):
    init_and_load_song(song)
    pygame.mixer.music.pause()


def unpause_song(song):
    init_and_load_song(song)
    pygame.mixer.music.unpause()


def rewind_song(song):
    init_and_load_song(song)
    pygame.mixer.music.rewind()


def repeat_song(song):
    PLAY_SONG_INFINITELY = -1
    init_and_load_song(song)
    pygame.mixer.music.play(PLAY_SONG_INFINITELY)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def play_next_song(song):
    pass


def play_previous_song(song):
    pass


def volume():
    pass


play_song("songs/bensound-epic.mp3")
time.sleep(1)
stop_song()