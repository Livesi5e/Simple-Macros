# An Application to program your own macros and use them globally
#
# Does not support macro recording

import PySimpleGUI as sg
import pyautogui as pag
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import keyboard
import json
from scripts.charSelect import charSelector

# Inital variables

list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Middle", "Right")
amm = ("Single", "Multiple")
cr = []
htky = ''
hotkeys = []
macros = []
sel=''
sel_mac = ''
view = "Nothing here yet"
font = ("Arial", 12)
visible = False
multiple = False
single = True
save = ''

# All window components

root = tkinter.Tk()
root.withdraw()

one = [
    [
        sg.T("Choose a keypress: "),
        sg.Button(button_text=sel, key='-cho-')
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
    [
        sg.InputText(key="-crn-", size=(10, 20), visible=False),
        sg.Button(button_text='Hotkey', key='-htk-', visible=False),
        sg.T(htky, visible=False, key='-hts-'),
        sg.Submit(button_text="Create", key='-cre-', visible=False)
    ]
]

your_macros = [
    [
        sg.Table(
            values=macros,
            headings=['Macros', 'Hotkey'],
            num_rows=10,
            alternating_row_color='green',
            key='-mac-',
            enable_events=True,
            justification='center',
        )
    ],
    [sg.Button(button_text='New', key='-new-'), sg.Button(button_text='Delete', key='-del-'), sg.Submit(button_text='Run', key='-run-'), sg.Button(button_text='Load', key='-lod-'), sg.Button(button_text='Save', key='-sve-')]
]

# ------ Full layout ------

layout = [
    [
        sg.pin(sg.Column(new_macro, visible=False, key='-left-')),
        sg.VerticalSeparator(),
        sg.pin(sg.Column(current_macro, visible=False, key='-mid-')),
        sg.VerticalSeparator(),
        sg.pin(sg.Column(your_macros, key="-ymc-"))
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
        elif x[0] == 1:
            key = ''
            match x[1]:
                case 3:
                    key = 'LMB'
                case 4:
                    key = 'RMB'
                case 5:
                    key = 'MMB'
            old = temp + 'Mouse Button Click at\n' + 'x: ' + str(x[2]) + ' ' + 'y: ' + str(x[3]) + '\nKey: ' + key + '\nAmmount of Clicks: ' + str(x[4]) + '\nTime between clicks: ' + str(x[5]) + '\n\n'
        elif x[0] == 2:
            try:
                old = temp + 'Keyboard Input:\n' + x[1] + '\n\n'
            except:
                old = temp + 'Keyboard Input:\n' + x[1][0] + '\n\n'
    return old

def Reset():
    window['-akmi-'].update('')
    window['-amm-'].update('Single')
    window['-mcb-'].update('-none-')
    window['-mcx-'].update('')
    window['-mcy-'].update('')
    window['-mmx-'].update('')
    window['-mmy-'].update('')

def ResetAdv():
    window['-mca-'].update('')
    window['-mct-'].update('')

def load(save):
    i = 0
    with open(save, 'r') as f:
        text = f.read()
        macros = json.loads(text)
    for x in macros:
        keyboard.add_hotkey(x[1], lambda x = i: Run(macros[x]))
        i += 1
    return macros

def toggle(change):
    if change == True:
        change = False
    else:
        change = True
    return change

def Run(mac):
    for x in mac[2]:
        match x[0]:
            case 0:
                pag.moveTo(x[1], x[2], 0.5)
            case 1:
                if x[1] == 3:
                    button = 'left'
                elif x[1] == 4:
                    button = 'right'
                elif x[1] == 5:
                    button = 'middle'
                pag.click(x=x[2], y=x[3], clicks=x[4], interval=x[5],button=button)
            case 2:
                pag.typewrite(x[1])
            case _:
                print('NaN')

def get_Hotkey():
    temp = keyboard.read_hotkey()
    return temp

# ------ Event Loop ------
#   Window will check for user inputs and 
#   respond accordingly. Check for update
#   is passive
#   
#       event is the ID of the user input and 
#       values are the values for every component
#       in the window

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
    elif event == "-new-":
        window['-left-'].update(visible=True)
        window['-mid-'].update(visible=True)
    elif event == "-cat-":
        new_add = []
        combo = values["-cat-"]
        Reset()
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
        ResetAdv()
        window["-adv-"].update(visible=visible)
    elif event == "-amm-":
        if values["-amm-"] == 'Single':
            single = True
            multiple = False
            window['-amm-'].update('Single')
            window["-akm-"].update(visible=multiple)
            window["-aks-"].update(visible=single)
        else:
            single = False
            multiple = True
            window['-amm-'].update('Multiple')
            window["-aks-"].update(visible=single)
            window["-akm-"].update(visible=multiple)
    elif event == "-am-":
        if values['-mmx-'] != '' and values['-mmy-'] != '':
            cr.append([0, int(values['-mmx-']), int(values['-mmy-'])])
            Reset()
            view = UpdateMid()
            window['-cur-'].update(view)
            window['-cre-'].update(visible=True)
            window['-crn-'].update(visible=True)
            window['-htk-'].update(visible=True)
            window['-hts-'].update(visible=True)
        else:
            messagebox.showerror('Warning', 'Please add values and retry')
    elif event == "-ac-":
        if values['-mcx-'] != '' and values['-mcy-'] != '' and values['-mcb-'] != '':
            Reset()
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
                time = float(values['-mct-'])
            cr.append([1, button, int(values['-mcx-']), int(values['-mcy-']), amt, time])
            view = UpdateMid()
            window['-cre-'].update(visible=True)
            window['-crn-'].update(visible=True)
            window['-htk-'].update(visible=True)
            window['-hts-'].update(visible=True)
            window['-cur-'].update(view)
        else:
            messagebox.showerror('Warning', 'Please add values and retry')
    elif event == '-ak-':
        Reset()
        if values['-amm-'] == 'Single':
            if sel != 'Nothing selected' and sel != '':
                cr.append([2, [sel]])
                view = UpdateMid()
                window['-cur-'].update(view)
                window['-cre-'].update(visible=True)
                window['-crn-'].update(visible=True)
                window['-htk-'].update(visible=True)
                window['-hts-'].update(visible=True)
            else:
                messagebox.showerror('Warning', 'Please select a character and try again')
        elif values['-amm-'] == 'Multiple':
            if values['-akmi-'] != '':
                cr.append([2, values['-akmi-']])
                view = UpdateMid()
                window['-cur-'].update(view)
                window['-cre-'].update(visible=True)
                window['-crn-'].update(visible=True)
                window['-htk-'].update(visible=True)
                window['-hts-'].update(visible=True)
            else:
                messagebox.showerror('Warning', 'Please enter a text and try again')
    elif event == "-cre-":
        if values['-crn-'] != '':
            macros.append([values['-crn-'], htky, cr])
            keyboard.add_hotkey(htky, lambda x = len(macros) - 1: Run(macros[x]))
            cr = []
            view = "Nothing here yet"
            window['-crn-'].update('')
            window['-mac-'].update(values=macros)
            window['-cre-'].update(visible=False)
            window['-crn-'].update(visible=False)
            window['-htk-'].update(visible=False)
            window['-hts-'].update(visible=False)
            window['-cur-'].update(view)
            window['-left-'].update(visible=False)
            window['-mid-'].update(visible=False)
        else:
            messagebox.showinfo('Provide a name', 'Please provide a name to the Macro')
    elif event == '-cho-':
        sel = charSelector()
        window['-cho-'].update(sel)
    elif event == '-del-':
        sel_mac = [macros[row] for row in values['-mac-']]
        try:
            macros.remove(sel_mac[0])
            keyboard.remove_hotkey(sel_mac[0][3])
        except:
            messagebox.showinfo('Warning', 'Select an entry to delete')
        window['-mac-'].update(values=macros)
    elif event == '-run-':
        sel_mac = [macros[row] for row in values['-mac-']]
        try:
            Run(sel_mac[0])
        except:
            messagebox.showinfo('Warning', 'Select an entry to run')
    elif event == '-htk-':
        htky = ''
        htky = get_Hotkey()
        window['-hts-'].update(htky)
    elif event == '-lod-':
        save = askopenfilename(filetypes=[("Macro files", "*.macros")])
        if save != '':
            macros = load(save)
        window['-mac-'].update(values=macros)
    elif event == '-sve-':
        f = asksaveasfile(mode='w', defaultextension='.macros', filetypes=[("Macro files", "*.macros")])
        if f != None:
            text2save = json.dumps(macros)
            f.write(text2save)
            f.close()

window.close()