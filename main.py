import curses

def main(stdscr):

    # setup screen
    curses.curs_set(0) # hide cursor
    stdscr.nodelay(1) # make getch() non-blocking
    stdscr.timeout(100) # set getch() timeout in ms

    # main loop
    while True:
        
        # clear screen
        stdscr.clear()
        
        # get user input
        key = stdscr.getch()

        # quit program if the user presses q
        if key == ord('q'):
            break
        
        # perform actions based on user input
        if key == ord('p'):
            play_music()
        elif key == ord('s'):
            stop_music()
        elif key == ord('n'):
            next_track()
        elif key == ord('p'):
            previous_track()

        # render screen
        render_interface(stdscr)

        # refresh screen
        stdscr.refresh()

def render_interface(stdscr):
    # render interface here
    # ex: stdscr.addstr(0, 0, "rattle music player")
    # use curses functions to position text and elements on the screen

def play_music():
    # to do

def stop_music():
    # to do

def next_track():
    # to do

def previous_track():
    # to do

if __name__ == "__main__":
    curses.wrapper(main)

