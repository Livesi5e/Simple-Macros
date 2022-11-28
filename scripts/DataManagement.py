import json
import os
import PySimpleGUI as sg
from tkinter.filedialog import asksaveasfile

def save(inp):
    f = asksaveasfile(mode='wb', defaultextension='.macros', filetypes=[("Macro Files", '*.macros')])
    if f == None:
        return
    final = []
    for x in inp:
        final.append(6)
        for y in x[0]:
            final.append(ord(y))
        final.append(6)
        for y in x[1]:
            final.append(ord(y))
        final.append(6)
        for y in x[2]:
            final.append(8)
            if y[0] == 0:
                final.append(0)
                for z in str(y[1]):
                    final.append(ord(str(z)))
                final.append(7)
                for z in str(y[2]):
                    final.append(ord(str(z)))
                final.append(7)
            elif y[0] == 1:
                final.append(1)
                if y[1] == 3:
                    final.append(3)
                elif y[1] == 4:
                    final.append(4)
                else:
                    final.append(5)
                for z in str(y[2]):
                    final.append(ord(z))
                final.append(7)
                for z in str(y[3]):
                    final.append(ord(z))
                final.append(7)
                for z in str(y[4]):
                    final.append(ord(z))
                final.append(7)
                for z in str(y[5]):
                    final.append(ord(z))
                final.append(7)
            elif y[0] == 2:
                final.append(2)
                for z in y[1]:
                    final.append(ord(z))
                final.append(7)
    f.write(bytes(final))
    f.close()

def convToInt(cur):
    for x in cur:
        for y in x[2]:
            if y[0] == 0:
                y[1] = int(y[1])
                y[2] = int(y[2])
            elif y[0] == 1:
                y[2] = int(y[2])
                y[3] = int(y[3])
                y[4] = int(y[4])
                y[5] = float(y[5])
    return cur


# !!! Never remove this function !!!
# 
# This function can read old savefiles and will be able to read all possible versions
# It will grow with new file structures of the .macros file
def legacy(file, add, old):
    cur = []

    layout = [
        [sg.T('It looks like you try to open a file saved in the old format.\nPlease load this file and re-save it to update your savefile!')],
        [sg.Button('Okay', key='-ok-')]
    ]

    window = sg.Window('Old File', layout)

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case '-ok-':
                if add:
                    with open(file, 'r') as f:
                        loaded = json.loads(f.read())
                        cur = old
                        for x in loaded:
                            cur.append(x)
                else:
                    with open(file, 'r') as f:
                        loaded = json.loads(f.read())
                        for x in loaded:
                            cur.append(x)
                break
    window.close()
    return cur

def load(save, cur):
    layout = [
        [sg.T('Do you want to merge your Macros with the savefile?')],
        [sg.Button('Yes', key='-yes-'), sg.Button('No', key='-noo-')]
        ]

    window = sg.Window('Attention', layout)

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case '-yes-':
                with open(save, 'rb') as f:
                    state = 2
                    num = 0
                    arr = 0
                    curr = ''
                    first = True
                    for x in f.read():
                        if x == 91 and first == True:
                            window.close()
                            return legacy(save, True, cur)
                        if x == 6 and state == 2:
                            state = 0
                            arr = 0
                            cur.append([])
                            num = len(cur) - 1
                        elif x == 6 and state == 1:
                            state += 1
                            cur[num].append([])
                        elif x == 6:
                            state += 1
                        else:
                            if state == 0:
                                try:
                                    cur[num][0] += chr(x)
                                except:
                                    cur[num].append(chr(x))
                            elif state == 1:
                                try:
                                    cur[num][1] += chr(x)
                                except:
                                    cur[num].append(chr(x))
                            elif state == 2:
                                if x == 8:
                                    cur[num][2].append([])
                                    arr = len(cur[num][2]) - 1
                                elif x == 7:
                                    cur[num][2][arr].append(curr)
                                    curr = ''
                                else:
                                    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                                        if x == 0:
                                            i = 0
                                        elif x == 1:
                                            i = 1
                                        elif x == 2:
                                            i = 2
                                        elif x == 3:
                                            i = 3
                                        elif x == 4:
                                            i = 4
                                        elif x == 5:
                                            i = 5
                                        cur[num][2][arr].append(i)
                                    else:
                                        curr += chr(x)
                        first = False
                    cur = convToInt(cur)
                break
            case '-noo-':
                cur = []
                with open(save, 'rb') as f:
                    state = 2
                    num = 0
                    arr = 0
                    curr = ''
                    first = True
                    for x in f.read():
                        if x == 91 and first == True:
                            window.close()
                            return legacy(save, False, cur)
                        if x == 6 and state == 2:
                            state = 0
                            arr = 0
                            cur.append([])
                            num = len(cur) - 1
                        elif x == 6 and state == 1:
                            state += 1
                            cur[num].append([])
                        elif x == 6:
                            state += 1
                        else:
                            if state == 0:
                                try:
                                    cur[num][0] += chr(x)
                                except:
                                    cur[num].append(chr(x))
                            elif state == 1:
                                try:
                                    cur[num][1] += chr(x)
                                except:
                                    cur[num].append(chr(x))
                            elif state == 2:
                                if x == 8:
                                    cur[num][2].append([])
                                    arr = len(cur[num][2]) - 1
                                elif x == 7:
                                    cur[num][2][arr].append(curr)
                                    curr = ''
                                else:
                                    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                                        if x == 0:
                                            i = 0
                                        elif x == 1:
                                            i = 1
                                        elif x == 2:
                                            i = 2
                                        elif x == 3:
                                            i = 3
                                        elif x == 4:
                                            i = 4
                                        elif x == 5:
                                            i = 5
                                        cur[num][2][arr].append(i)
                                    else:
                                        curr += chr(x)
                        first = False
                    cur = convToInt(cur)
                break

    # ------ After Eventloop ------
    #   Window will be closed, value will be returned and script ends

    window.close()
    return cur

def saveStart(inp):
    path = os.path.expanduser('~\AppData\Roaming\SimpleMacro')
    if os.path.isdir(path) != True:
        os.mkdir(path)
    path = os.path.join(path, 'save.macros')
    with open(path, mode='wb') as f:
        final = []
        for x in inp:
            final.append(6)
            for y in x[0]:
                final.append(ord(y))
            final.append(6)
            for y in x[1]:
                final.append(ord(y))
            final.append(6)
            for y in x[2]:
                final.append(8)
                if y[0] == 0:
                    final.append(0)
                    for z in str(y[1]):
                        final.append(ord(str(z)))
                    final.append(7)
                    for z in str(y[2]):
                        final.append(ord(str(z)))
                    final.append(7)
                elif y[0] == 1:
                    final.append(1)
                    if y[1] == 3:
                        final.append(3)
                    elif y[1] == 4:
                        final.append(4)
                    else:
                        final.append(5)
                    for z in str(y[2]):
                        final.append(ord(z))
                    final.append(7)
                    for z in str(y[3]):
                        final.append(ord(z))
                    final.append(7)
                    for z in str(y[4]):
                        final.append(ord(z))
                    final.append(7)
                    for z in str(y[5]):
                        final.append(ord(z))
                    final.append(7)
                elif y[0] == 2:
                    final.append(2)
                    for z in y[1]:
                        final.append(ord(z))
                    final.append(7)
        f.write(bytes(final))



def loadStart():
    final = []
    try:
        path = os.path.expanduser('~\AppData\Roaming\SimpleMacro')
        if os.path.isdir(path) != True:
            os.mkdir(path)
        path = os.path.join(path, 'save.macros')
        with open(path, mode='rb') as f:
            cur = []
            state = 2
            num = 0
            arr = 0
            curr = ''
            for x in f.read():
                if x == 6 and state == 2:
                    state = 0
                    arr = 0
                    cur.append([])
                    num = len(cur) - 1
                elif x == 6 and state == 1:
                    state += 1
                    cur[num].append([])
                elif x == 6:
                    state += 1
                elif x == 10:
                    final.append(False)
                elif x == 9:
                    final.append(True)
                else:
                    if state == 0:
                        try:
                            cur[num][0] += chr(x)
                        except:
                            cur[num].append(chr(x))
                    elif state == 1:
                        try:
                            cur[num][1] += chr(x)
                        except:
                            cur[num].append(chr(x))
                    elif state == 2:
                        if x == 8:
                            cur[num][2].append([])
                            arr = len(cur[num][2]) - 1
                        elif x == 7:
                            cur[num][2][arr].append(curr)
                            curr = ''
                        else:
                            if x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                                if x == 0:
                                    i = 0
                                elif x == 1:
                                    i = 1
                                elif x == 2:
                                    i = 2
                                elif x == 3:
                                    i = 3
                                elif x == 4:
                                    i = 4
                                elif x == 5:
                                    i = 5
                                cur[num][2][arr].append(i)
                            else:
                                curr += chr(x)
        final = convToInt(cur)
    except:
        return []
    return final

# ------ Test code ------

if __name__ == '__main__':
    test = load()