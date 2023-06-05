import curses

import os

def get_files(directory):
    files = os.listdir(directory)

    return [f for f in files if os.path.isfile(os.path.join(directory, f))]

def draw_file_list(stdscr, file_list, selected_index):
    stdscr.clear()

    height, width = stdscr.getmaxyx()

    for i, file_name in enumerate(file_list):
        if i == selected_index:
            stdscr.attron(curses.A_REVERSE)
        else:
            stdscr.attroff(curses.A_REVERSE)

        stdscr.addstr(i, 0, file_name)

    stdscr.refresh()




def main(stdscr):

    stdscr.keypad(True)
    curses.curs_set(0)

    current_dir = os.path.expanduser('~/Música/')
    file_list = get_files(current_dir)
    selected_index = 0

    while True:
        
        draw_file_list(stdscr, file_list, selected_index)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_index = max(0, selected_index - 1)
        elif key == curses.KEY_DOWN:
            selected_index = min(len(file_list) - 1, selected_index + 1)
        elif key == ord('\n'): # enter key
            selected_file = file_list[selected_index]
            #play the song

        new_dir = os.path.join(current_dir, file_list[selected_index])
        if os.path.isdir(new_dir):
            current_dir = new_dir
            file_list = get_files(current_dir)
            selected_index = 0

curses.wrapper(main)
