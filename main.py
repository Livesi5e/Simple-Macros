# An Application to program your own macros and use them globally
#
# Does not support recording

import PySimpleGUI as sg
import tkinter
from tkinter import messagebox

# Inital variables

list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Middle", "Right")
amm = ("Single", "Multiple")
keys = ()
cr = []
view = "Add values on the left to see them here"
font = ("Arial", 12)
visible = False
multiple = False
single = True

# All window components

root = tkinter.Tk()
root.withdraw()

one = [
    [
        sg.T("Choose a keypress here: "),
        sg.Combo(values=keys, size=(10, len(keys)), default_value="-none-", key="-aksi-", enable_events=True, readonly=True)
    ]
]

more = [
    [
        sg.T("Type here: "),
        sg.InputText(key="-akmi-", size=(10, 20))
    ]
]

add_key = [
    [sg.T('')],
    [
        sg.T("Ammount of Charakters: "),
        sg.Combo(values=amm, size=(10, len(amm)), default_value="Single", key="-amm-", enable_events=True, readonly=True),
    ],
    [
        sg.pin(sg.Column(one, visible=single, key='-aks-'))
    ],
    [
        sg.pin(sg.Column(more, visible=multiple, key='-akm-'))
    ],
    [
        sg.Submit(button_text="Add", key="-ak-"),
    ]
]

add_click_adv = [
    [
        sg.T("Ammount of clicks:"),
        sg.InputText(key="-mca-", size=(10, 20))
    ],
    [
        sg.T("Time between clicks:"),
        sg.InputText(key="-mct-", size=(10, 20))
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
        sg.pin(sg.Column(add_click_adv, visible=False, key="-adv-")),
    ],
    [
        sg.Submit(button_text="Add", key="-ac-"),
        sg.Submit(button_text="Advanced", key="-aca-")
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
    [sg.Submit(button_text="Create", key='-cre-', visible=False)]
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
            match x[1]:
                case 3:
                    key = 'LMB'
                case 4:
                    key = 'RMB'
                case 5:
                    key = 'MMB'
            old = temp + 'Mouse Button Click at\n' + 'x: ' + str(x[2]) + ' ' + 'y: ' + str(x[3]) + '\nKey: ' + key + '\nAmmount of Clicks: ' + str(x[4]) + '\nTime between clicks: ' + str(x[5]) + '\n\n'
    return old

def Clear():
    print('test')

def toggle(change):
    if change == True:
        change = False
    else:
        change = True
    return change

# ------ Event Loop ------

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
    elif event == "-aca-":
        visible = toggle(visible)
        window["-adv-"].update(visible=visible)
    elif event == "-amm-":
        if values["-amm-"] == 'Single':
            single = True
            multiple = False
            window["-akm-"].update(visible=multiple)
            window["-aks-"].update(visible=single)
        else:
            single = False
            multiple = True
            window["-aks-"].update(visible=single)
            window["-akm-"].update(visible=multiple)
    elif event == "-am-":
        if values['-mmx-'] != '' and values['-mmy-'] != '':
            cr.append([0, int(values['-mmx-']), int(values['-mmy-'])])
            view = UpdateMid()
            window['-cur-'].update(view)
            window['-cre-'].update(visible=True)
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
                case 'Middle':
                    button = 5
                case _:
                    break
            amt = 0
            time = 0
            if values['-mca-'] == '':
                amt = 1
            else:
                amt = int(values['-mca-'])
            if values['-mct-'] == '':
                time = 0.2
            else:
                time = int(values['-mct-'])
            cr.append([1, button, int(values['-mcx-']), int(values['-mcy-']), amt, time])
            view = UpdateMid()
            window['-cre-'].update(visible=True)
            window['-cur-'].update(view)
        else:
            messagebox.showerror('Warning', 'Please add values and retry')

window.close()