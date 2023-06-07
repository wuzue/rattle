from pygame import mixer
import pygame
import os
import curses
from mutagen.mp3 import MP3
import random
import numpy as np

def play_song(file_path, stdscr):
    
    mixer.init()
    pygame.init()
    pygame.mixer.init()

    mixer.music.load(file_path)
    mixer.music.set_volume(0.5)
    mixer.music.play()
    
    audio = MP3(file_path)
    total_time = int(audio.info.length)

    stdscr.nodelay(True) # set non-blocking mode for input 
    stdscr.timeout(100) # set input timeout to 100 ms

    progress_bar_length = 20

    # detect current song
    file_name = os.path.basename(file_path)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Now playing: {file_name}")
        stdscr.addstr(1, 0, "Press P to pause, R to resume and E to exit the program")

        # calculate time remaining
        elapsed_time = mixer.music.get_pos() / 1000
        remaining_time = total_time - elapsed_time

        # format the time remaining as minutes:seconds
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        time_remaining = f"Time Remaining: {minutes:02d}:{seconds:02d}"

        # calculate the progress bar
        progress = int((elapsed_time / total_time) * progress_bar_length)
        progress_bar = "[" + "#" * progress + "-" * (progress_bar_length - progress) + "]"

        # display time remaining and progress bar
        stdscr.addstr(2, 0, time_remaining)
        stdscr.addstr(4, 0, progress_bar)

        key = stdscr.getch()
    
        if key == ord('p'):
            if mixer.music.get_pos() > 0: # check if song has been played
                mixer.music.pause()
        elif key == ord('r'):
            if mixer.music.get_pos() > 0: # check if song has been played
                mixer.music.unpause()
        elif key == ord('e'):
            mixer.music.stop()
            break
    
              
        stdscr.refresh()

    pygame.quit()

        
