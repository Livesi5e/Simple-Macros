def convert(x):
    finished = True
    hotkey = ''
    i = 14
    while finished:
        hotkey += str(x)[i].lower()
        i += 1
        if str(x)[i] == ' ':
            finished = False
    return hotkey