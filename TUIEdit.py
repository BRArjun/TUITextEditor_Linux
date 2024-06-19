#!/usr/bin/env python3

import curses
import sys
import time
import os
import subprocess
import atexit

# Path to the flag file
flag_file = "/tmp/terminal_command_executed.flag"

# Function to delete the flag file
def remove_flag_file():
    if os.path.exists(flag_file):
        os.remove(flag_file)

# Check if the flag file exists
if not os.path.exists(flag_file):
    # Command to be executed
    command = "cd ~; cd TUIText; python3 TUIEdit.py; exec bash"

    # Open a new terminal and execute the command
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', command])

    # Create the flag file to prevent further executions
    with open(flag_file, 'w') as f:
        f.write("Executed")
else:
    # If the flag file exists
    remove_flag_file()
    pass
    
class MicroEditor:

    def __init__(self):
        self.window = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        self.window.keypad(1)
        self.window.clear()
        greetmessage="Yo! Thanks for using this TUI text editor that I made. Kudos to the Python curses library and its documentation.\n"
        for char in greetmessage:
            self.window.addstr(char)
            self.window.refresh()
            time.sleep(0.1)
        self.window.addstr("To exit use Esc+q\nTo save use Esc+s\nTo save and exit use Esc+x\nTo open a file for viewing/editing use Esc+o\n\n")
        self.window.refresh()
        self.window.addstr("Start your input in 3...\n")
        self.window.refresh()
        time.sleep(2)
        self.window.addstr("2...\n")
        self.window.refresh()
        time.sleep(2)
        self.window.addstr("1...\n")
        self.window.refresh()
        time.sleep(2)
        self.window.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        curses.nocbreak()
        self.window.keypad(0)
        curses.echo()
        curses.endwin()

    def save(self, exit):
        content = ''
        y, x = self.window.getmaxyx()
        for y_coord in range(y):
            line = self.window.instr(y_coord, 0).rstrip().decode('utf-8')
            if line != '':
                content += line + '\n'  # Add newline after each line
            else:
                break
        
        filename = self.get_filename()  # Get the filename from user input
        if filename is None:
            return  # Handle the case where filename is not provided
        else:
            with open(filename, 'w') as f:
                f.write(content)
                f.close()
                curses.endwin()
                sys.exit()

    def get_filename(self):
        self.window.clear()  # Clear the window to get clean input
        self.window.addstr("What do you want your file to be named as?\n")
        self.window.refresh()
        curses.echo()  # Enable echo to capture user input
        nameoffile = self.window.getstr().decode('utf-8').strip()
        curses.noecho()
        return nameoffile if nameoffile else "untitled.txt"  # Return filename or a default if empty
        
    def get_filename_for_opening(self):
        self.window.clear()  # Clear the window to get clean input
        self.window.addstr("What file do you want to open?\n")
        self.window.refresh()
        curses.echo()  # Enable echo to capture user input
        nameoffile = self.window.getstr().decode('utf-8').strip()
        curses.noecho()
        return nameoffile if nameoffile else "untitled.txt"  # Return filename or a default if empty

    def support_arrow_keys(self, key):
    	y, x = self.window.getyx()  # current cursor position
    	max_y, max_x = self.window.getmaxyx()  # dimensions of the window

    	if key == curses.KEY_DOWN:
        	new_y = min(y + 1, max_y - 1)
        	self.window.move(new_y, x)
    	elif key == curses.KEY_UP:
        	new_y = max(y - 1, 0)
        	self.window.move(new_y, x)
    	elif key == curses.KEY_LEFT:
        	new_x = max(x - 1, 0)
        	self.window.move(y, new_x)
    	elif key == curses.KEY_RIGHT:
        	new_x = min(x + 1, max_x - 1)
        	self.window.move(y, new_x)

    def edit(self):
        while True:
            key = self.window.getch()
            if key == 27:  # ESC key
                cmd = self.window.getch()
                if cmd == ord('q'):  # To quit: (ESC and q) OR (ALT + q)
                    break
                elif cmd == ord('s'):  # To save: (ESC and s) OR (ALT + s)
                    self.save('keep')
                elif cmd == ord('x'):  # To save and exit: (ESC and x) or (ALT + X)
                    self.save('die')
                elif cmd == ord('o'):
                    curses.endwin()
                    filename=self.get_filename_for_opening()
                    if filename:
                        self.view_file(filename)
            elif key == curses.KEY_BACKSPACE:
                y, x = self.window.getyx()
                if x > 0:
                    self.window.delch(y, x - 1)
            elif key < 127:
                self.window.addch(chr(key))
            else:
                self.support_arrow_keys(key)
    
    def view_file(self, filename):
        self.window.clear()  # Clear the window to display file content
        try:
            with open(filename, 'r') as f:
                readcontent = f.read()
                f.close()
                for char in readcontent:
                    self.window.addch(char)
                    self.window.refresh()
                    time.sleep(0.05) # Adjust this delay as needed for readability
        except:
            self.window.addstr("File not found: {}\n".format(filename))
            self.window.refresh()
            time.sleep(1)
            sys.exit()
        
        self.window.refresh()
        self.window.getch()  # Wait for user input to continue# Clear the window after displaying file content
        
if __name__ == '__main__':
    with MicroEditor() as micro:
        micro.edit()
