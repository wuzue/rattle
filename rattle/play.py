from pygame import mixer
import curses

def play_song(file_path, stdscr):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.set_volume(0.5)
    mixer.music.play()

    stdscr.nodelay(True) # set non-blocking mode for input 
    stdscr.timeout(100) # set input timeout to 100 ms

    while True:
        stdscr.clear()
        print("Press P to pause, R to resume and E to exit the program")

        key = stdscr.getch()
    
        if key == ord('p'):
            if mixer.music.get_busy():
                mixer.music.pause()
        elif key == ord('r'):
            if mixer.music.get_pos() > 0: # check if song has been played
                mixer.music.unpause()
        elif key == ord('e'):
            mixer.music.stop()
            break

