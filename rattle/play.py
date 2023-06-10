from pygame import mixer
import pygame
import os
import curses
from mutagen.mp3 import MP3

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
    
    current_dir = os.path.expanduser('~/Música/')

    def get_files(directory):
    # get a list of files in the specified directory
        files = os.listdir(directory)

    # filter out directories and return the file names
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]

    file_list = get_files(current_dir)
    current_song_index  = file_list.index(os.path.basename(file_path))


    while True:
        stdscr.clear()

        current_song = os.path.basename(file_path)
        next_song_index = (current_song_index + 1) % len(file_list)
        next_song = file_list[next_song_index]
        previous_song_index = (current_song_index - 1) % len(file_list)
        previous_song = file_list[previous_song_index]

        text_bold = f"Previous: {previous_song} | Now Playing: {current_song} | Next: {next_song}"
        stdscr.addstr(0, 0, text_bold, curses.A_BOLD | curses.COLOR_RED)

        stdscr.addstr(1, 0, "p = pause, r = resume, v = volume up, shift+v = volume down, n = next song, b = previous song, e = exit")

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
        
        # get current volume
        volume = int(mixer.music.get_volume() * 100)
        volume_display = f"Volume: {volume}%"
        stdscr.addstr(6, 0, volume_display)

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
        elif key == ord('v'):
            volume += 11 # increase volume by 10
            if volume > 100:
                volume = 100
            mixer.music.set_volume(volume / 100)
        elif key == ord('V'):
            volume -= 11 # decrease volume by 10
            if volume < 0:
                volume = 0
            mixer.music.set_volume(volume / 100)
        elif key == ord('n'):
            mixer.music.stop()
            next_song_index = (current_song_index + 1) % len(file_list)   
            next_song = file_list[next_song_index]
            play_song(os.path.join(current_dir, next_song), stdscr)
        elif key == ord('b'):
            mixer.music.stop()
            previous_song_index = (current_song_index - 1) % len(file_list)
            previous_song = file_list[previous_song_index]
            play_song(os.path.join(current_dir, previous_song), stdscr)

        stdscr.refresh()

    pygame.quit()
