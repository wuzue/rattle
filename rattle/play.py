from pygame import mixer
import pygame
import curses
from mutagen.mp3 import MP3
import random
import numpy as np

def play_song(file_path, stdscr):
    mixer.init()
    pygame.mixer.init()
    mixer.music.load(file_path)
    mixer.music.set_volume(0.5)
    mixer.music.play()

    audio = MP3(file_path)
    total_time = int(audio.info.length)

    stdscr.nodelay(True) # set non-blocking mode for input 
    stdscr.timeout(100) # set input timeout to 100 ms

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Press P to pause, R to resume and E to exit the program")

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
    
        # visualization: time remaining
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() // 1000 # convert miliseconds to seconds
            remaining_time = total_time - current_time
            stdscr.addstr(2, 0, "Time Remaining: {:02d}:{:02d}".format(remaining_time // 60, remaining_time % 60))

       
        stdscr.refresh()

    pygame.quit()

        
