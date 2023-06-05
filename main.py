import curses, os

from rattle.play import play_song

def get_files(directory):
    # get a list of files in the specified directory
    files = os.listdir(directory)

    # filter out directories and return the file names
    return [f for f in files if os.path.isfile(os.path.join(directory, f))]

def draw_file_list(stdscr, file_list, selected_index):
    # remember that stdscr = screen :)
    # here we clear it
    stdscr.clear()

    # get screen dimensions
    height, width = stdscr.getmaxyx()

    # display file names
    for i, file_name in enumerate(file_list):
        # set the text attributes based on whether the file is selected
        if i == selected_index:
            stdscr.attron(curses.A_REVERSE)
        else:
            stdscr.attroff(curses.A_REVERSE)
        
        # display the file name
        stdscr.addstr(i, 0, file_name)

    # refresh screen to display the changes
    stdscr.refresh()

def main(stdscr):
    # set the input mode
    stdscr.keypad(True)
    curses.curs_set(0)

    # set up the initial state
    current_dir = os.path.expanduser('~/Música/')
    file_list = get_files(current_dir)
    selected_index = 0

    while True:
        
        draw_file_list(stdscr, file_list, selected_index)

        # wait for user input 
        key = stdscr.getch()

        # handle movement inputs
        if key == curses.KEY_UP:
            selected_index = max(0, selected_index - 1)
        elif key == curses.KEY_DOWN:
            selected_index = min(len(file_list) - 1, selected_index + 1)
        elif key == ord('\n'): # enter key
            if file_list:
                selected_file = file_list[selected_index]
                file_path = os.path.join(current_dir, selected_file)
                play_song(file_path)
        
        # update file list if the current directory changes
        if file_list and selected_index < len(file_list):
            new_dir = os.path.join(current_dir, file_list[selected_index])
            if os.path.isdir(new_dir):
                current_dir = new_dir
                file_list = get_files(current_dir)
                selected_index = 0

        if key == ord('e'):
            break

curses.wrapper(main)
