from pynput import keyboard

def on_press(key):
    try:
        # Write code here to handle the keypress, e.g., log it to a file or database
        print(f'Key pressed: {key.char}')
    except AttributeError:
        # Some special keys (e.g., function keys, arrows) don't have a 'char' attribute
        print(f'Special key pressed: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Create and start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
