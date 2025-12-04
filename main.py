# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension (not strictly needed for just media keys, but good practice)
macros = Macros()
keyboard.modules.append(macros)

# --- Define Pins according to your 3x3 physical layout ---
# Pin Order:
# [R1C1, R1C2, R1C3, R2C1, R2C2, R2C3, R3C1, R3C2, R3C3]
# R1: SW1 (D7), SW4 (D6), SW7 (D26)
# R2: SW2 (D28), SW5 (D29), SW8 (D4)
# R3: SW3 (D3), SW6 (D27), SW9 (D2)
PINS = [
    board.D7, board.D6, board.D26,
    board.D28, board.D29, board.D4,
    board.D3, board.D27, board.D2
]

# Tell kmk we are not using a key matrix
# KeysScanner works for up to 10 pins on KMK
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, # Assumes switch pulls pin to GND
)

# --- Keymap Definition matching the 3x3 diagram ---
keyboard.keymap = [
    [
        # ROW 1 (Top)
        KC.AUDIO_VOL_UP,  # volume up
        KC.AUDIO_MUTE,   # volume cut (Mute)
        KC.AUDIO_VOL_DOWN,  # volume down

        # ROW 2 (Middle)
        KC.MPRV,   # previous song
        KC.UP,     # arrow up
        KC.MNXT,   # next song or item

        # ROW 3 (Bottom)
        KC.LEFT,   # arrow left
        KC.DOWN,   # arrow down
        KC.RIGHT,  # arrow right
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
