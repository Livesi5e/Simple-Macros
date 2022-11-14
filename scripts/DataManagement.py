import json
import keyboard
import PySimpleGUI as sg
from tkinter.filedialog import asksaveasfile

def save(inp):
    f = asksaveasfile(mode='wb', defaultextension='.macros', filetypes=[('Macro Files', '*.macros')])
    if f != None:
        i = 0
        tosave = []
        for x in inp:
            tosave.append(39)
            for y in x[0]:
                tosave.append(ord(y))
            tosave.append(39)
            for y in x[1]:
                tosave.append(ord(y))
            tosave.append(39)
            for y in x[2]:
                match y[0]:
                    case 0:
                        tosave.append(48)
                        tosave.append(ord(str(y[1])))
                        tosave.append(ord(str(y[2])))
                    case 1:
                        tosave.append(49)
                    case 2:
                        tosave.append(50)
        finalwrite = bytes(tosave)
        f.write(finalwrite)
        f.close()

def load(save, cur, Run):
    layout = [
        [sg.T('Do you want to merge your Macros with the savefile?')],
        [sg.Button('Yes', key='-yes-'), sg.Button('No', key='-noo-')]
        ]

    window = sg.Window('Attention', layout)

    while True:
        event, values = window.read()
        match event:
            case '-yes-':
                i = 0
                with open(save, 'r') as f:
                    text = f.read()
                    loaded = json.loads(text)
                    for x in loaded:
                        cur.append(x)
                for x in cur:
                    keyboard.add_hotkey(x[1], lambda x = i: Run(cur[x]))
                    i += 1
                break
            case '-noo-':
                i = 0
                with open(save, 'r') as f:
                    text = f.read()
                    cur = json.loads(text)
                for x in cur:
                    keyboard.add_hotkey(x[1], lambda x = i: Run(cur[x]))
                    i += 1
                break

    # ------ After Eventloop ------
    #   Window will be closed, value will be returned and script ends

    window.close()
    return cur

# ------ Test code ------

if __name__ == '__main__':
    test = load()