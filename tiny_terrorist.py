import keyboard
import time
import sys

exitProgram = False

print("Calculating damage...\nPress 'Enter' to stop.")


# prepare to exit the program
def quit():
    global exitProgram
    exitProgram = True


# set hotkey
keyboard.add_hotkey("enter", lambda: quit())

damage = 0
# Add 1 damage per second
while not exitProgram:
    damage += 1
    time.sleep(1)

print(f"Total amount of damage done: {damage} minutes of cleaning to do.")
sys.exit()
