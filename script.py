import curses
from curses import wrapper

def main(stdscr):

    #clears screen
    stdscr.clear()

    #output to screen
    stdscr.addstr("Hello World!")

    #refresh screen
    stdscr.refresh()

    #get key from user
    stdscr.getkey()
        
wrapper(main)
