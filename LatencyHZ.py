from pynput import mouse
import time

prev_time = time.perf_counter()
move_counter = 0

def on_move(x, y):
    global prev_time, move_counter
    curr_time = time.perf_counter()
    elapsed_time = curr_time - prev_time
    # Just for avoid division by zero, because it won't make sense
    if elapsed_time > 0:  
        hz = 1 / elapsed_time
        move_counter += 1
        if move_counter % 100 == 0:
            print(f'Mouse HZ: {hz:.0f} HZ' )
    prev_time = curr_time

with mouse.Listener(on_move=on_move) as listener:
    listener.join()
