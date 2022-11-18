from keyboard import KeyboardEvent

def convert(x):
    finished = True
    hotkey = ''
    i = 14
    while finished:
        hotkey += str(x)[i]
        i += 1
        if str(x)[i] == ' ':
            finished = False
    return hotkey