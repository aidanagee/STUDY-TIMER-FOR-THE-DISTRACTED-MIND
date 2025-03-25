import time
import keyboard

def countdown(t):
    print('Hit spacebar to exit...')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        if keyboard.is_pressed('space'):
            print('Exiting...')
            return



t = input('Enter the time in seconds: ')

countdown(int(t))
