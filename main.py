# An Application to program your own macros and use them globally
#
# Does not support recording

import PySimpleGUI as sg
import tkinter
from tkinter import messagebox

# Inital variables

list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Right")
keys = ()
cr = []
view = "Add values on the left to see them here"
font = ("Arial", 12)

# All window components

root = tkinter.Tk()
root.withdraw()

add_key = [
    [sg.T('')],
    [
        sg.T("Key: "),
        sg.Combo(values=keys, size=(10, len(keys)), default_value="-none-", key="-kik", enable_events=True, readonly=True)
    ],
    [
        sg.Submit(button_text="Add", key="-ak-"),
    ]
]

add_click = [
    [sg.T('')],
    [
        sg.T("Mouse Button: "),
        sg.Combo(values=mb, size=(10, len(mb)), default_value="-none-", key="-mcb-", enable_events=True, readonly=True)
    ],
    [
        sg.T("X-Coordinate: "),
        sg.InputText(key="-mcx-", size=(10, 20)),
    ],
    [
        sg.T("Y-Coordinate: "),
        sg.InputText(key="-mcy-", size=(10, 20)),
    ],
    [
        sg.Submit(button_text="Add", key="-ac-"),
    ]
]

add_movement = [
    [sg.T("")],
    [
        sg.T("X-Coordinate: "),
        sg.InputText(key="-mmx-", size=(10, 20)),
    ],
    [
        sg.T("Y-Coordinate: "),
        sg.InputText(key="-mmy-", size=(10, 20)),
    ],
    [
        sg.Submit(button_text="Add", key="-am-"),
    ]
]

new_macro = [
    [
        sg.T("Input type: "),
        sg.Combo(values=list, size=(15, len(list)), default_value="Pick Input Type", key="-cat-", enable_events=True, readonly=True),
    ],
    [
        sg.pin(sg.Column(add_movement, key="-mousemove-", visible=False)),
        sg.pin(sg.Column(add_click, key="-mouseclick-", visible=False)),
        sg.pin(sg.Column(add_key, key="-keyinp-", visible=False)),
    ],
]

current_macro = [
    [sg.T("Current Macro: ", font=font)],
    [sg.T(view, key='-cur-')],
    [sg.Submit(button_text="Create", key='-cre-')]
]

# ------ Full layout ------

layout = [
    [
        sg.Column(new_macro),
        sg.VerticalSeparator(),
        sg.Column(current_macro),
    ]
]

window = sg.Window("Simple Macros", layout)

# ------ Functions ------

def UpdateMid():
    old = ''
    for x in cr:
        temp = old
        if x[0] == 0:
            old = temp + 'Mouse Movement to\n' + 'x: ' + str(x[1]) + ' ' + 'y: ' + str(x[2]) + '\n\n'
        if x[0] == 1:
            key = ''
            if x[1] == 3:
                key = 'LMB'
            if x[1] == 4:
                key = 'RMB'
            old = temp + 'Mouse Button Click at\n' + 'x: ' + str(x[2]) + ' ' + 'y: ' + str(x[3]) + '\nKey: ' + key + '\n' + '\n\n'
    return old

def Clear():
    print('test')

# ------ Event Loop ------
# ID-List:
# 
# 0 - Mouse Movement
# 1 - Mouse Click
# 2 - Keyboard Input
#
# 3 - Left MB
# 4 - Right MB

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
    elif event == "-cat-":
        new_add = []
        combo = values["-cat-"]
        if combo == 'Mouse Movement':
            window["-keyinp-"].update(visible=False)
            window["-mouseclick-"].update(visible=False)
            window["-mousemove-"].update(visible=True)
        if combo == 'Mouse Click':
            window["-keyinp-"].update(visible=False)
            window["-mousemove-"].update(visible=False)
            window["-mouseclick-"].update(visible=True)
        if combo == 'Keyboard Input':
            window["-mousemove-"].update(visible=False)
            window["-mouseclick-"].update(visible=False)
            window["-keyinp-"].update(visible=True)
    elif event == "-am-":
        if values['-mmx-'] != '' and values['-mmy-'] != '':
            cr.append([0, int(values['-mmx-']), int(values['-mmy-'])])
            view = UpdateMid()
            window['-cur-'].update(view)
        else:
            messagebox.showerror('Warning', 'Please add values and retry')
    elif event == "-ac-":
        if values['-mcx-'] != '' and values['-mcy-'] != '' and values['-mcb-'] != '':
            button = 0
            match values['-mcb-']:
                case 'Left':
                    button = 3
                case 'Right':
                    button = 4
                case _:
                    break
            cr.append([1, button, int(values['-mcx-']), int(values['-mcy-'])])
            view = UpdateMid()
            window['-cur-'].update(view)
        else:
            messagebox.showerror('Warning', 'Please add values and retry')

window.close()