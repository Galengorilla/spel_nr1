import sys
from time import sleep
import msvcrt # Importing the msvcrt module for non-blocking keyboard input on Windows
from os import system

def letters(words):
    for x in words:
        # Print each character of the string without newline
        sys.stdout.write(x)
        # Flush the output buffer to ensure immediate printing
        sys.stdout.flush()
        sleep(0.2)
        # Check if a key has been pressed
        if msvcrt.kbhit(): # kbhit() returns True if a key is pressed, without blocking
            # Get the key pressed
            key = msvcrt.getch()
            # Check if the Enter key (represented as b'\r') is pressed
            if key == b'\r':
                system('cls')
                print(words)
                # Exit the loop, skipping the rest of the string
                break

letters("Hello you little animal what are you doing")
