import curses
from curses import wrapper
import time

def start_program(stdscr):
    #clears screen
    stdscr.clear()

    #output to screen
    stdscr.addstr("Welcome to Words Per Minute Program!")
    stdscr.addstr("\nPress any key to begin!")

    #refresh screen
    stdscr.refresh()

    #get key from user
    key = stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"wpm: {wpm}")

    #overlay current characterst to target characters
    for i,char in enumerate(current):

        #Correct Character
        correct_char = target[i]

        #colors -> green
        color = curses.color_pair(1)

        #if char is different change color to red
        if char != correct_char:
            color = curses.color_pair(2)

        #add character over target character
        stdscr.addstr(0, i, char, color)

   
def wpm_test(stdscr):
    #variables
    target_text = "Hello World this is some test text for this app!"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    #clearing screen and adding target text to screen
    stdscr.clear()
    stdscr.addstr(target_text)

    while True:
        #calculate time elapsed
        time_elapsed = max(time.time() - start_time, 1)

        #calculating words per minute
        wpm = round(len(current_text) / (time_elapsed/60)
)
        #clearing Screen
        stdscr.clear()

        #display text to screen
        display_text(stdscr, target_text, current_text, wpm)
        
        #refreshing screen
        stdscr.refresh()

        #get final current text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        #For calculating WPM 
        try:
            #get user key input
            key = stdscr.getkey()
        except:
            continue

        #if escape button hit -> exit program
        if key == '\x1b': #Linux Terminal
            break

        #deleting characters    
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        #does not allow user to go past the target text
        elif len(current_text) < len(target_text):
            current_text.append(key)
    


def main(stdscr):

    #init curses colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    #app
    start_program(stdscr)
    
    while True:

        wpm_test(stdscr)

        stdscr.addstr(2,0, "You completed the text! Press any key to continue... (ESC to exit)")
        
        key = stdscr.getkey()

        if key == '\x1b':
            break

wrapper(main)
