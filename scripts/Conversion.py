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

def UpdateMid(x):
    text = []
    for y in x:
        text.append([])
        match y[0]:
            case 0:
                text[len(text)-1].append([y[3], '.'])
                text[len(text)-1].append('Mouse Movement')
                text[len(text)-1].append(str(y[1]))
                text[len(text)-1].append(str(y[2]))
                text[len(text)-1].append('')
                text[len(text)-1].append('')
                text[len(text)-1].append('')
            case 1:
                text[len(text)-1].append([y[6], '.'])
                text[len(text)-1].append('Mouse Click')
                text[len(text)-1].append(str(y[2]))
                text[len(text)-1].append(str(y[3]))
                match y[1]:
                    case 3:
                        text[len(text)-1].append('LMB')
                    case 4:
                        text[len(text)-1].append('RMB')
                    case 5:
                        text[len(text)-1].append('MMB')
                text[len(text)-1].append(str(y[4]))
                text[len(text)-1].append(str(y[5]))
            case 2:
                text[len(text)-1].append([y[2], '.'])
                text[len(text)-1].append('Keyboard Input')
                text[len(text)-1].append('')
                text[len(text)-1].append('')
                text[len(text)-1].append(y[1])
                text[len(text)-1].append('')
                text[len(text)-1].append('')

    return text

def UpdateList(macros, active):
    data = []
    for x, y in zip(macros, active):
        data.append([x[0], x[1], y])
    return data