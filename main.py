# An Application to program your own macros and use them globally
#
# Does not support macro recording

import PySimpleGUI as sg
import pyautogui as pag
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import keyboard
import enableStartup
from scripts.charSelect import charSelector
from scripts.DataManagement import load, save, saveStart, loadStart
from scripts.Conversion import convert, UpdateMid
from scripts.macros import Run, load_hotkeys

# Inital variables

startup = True
list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Middle", "Right")
amm = ("Single", "Multiple")
curhead=("ID", "     Type     ", "   X   ", "   Y   ", "   Key   ", "Clicks", "Time")
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

# ------ Startup ------

loaded = loadStart()
startup = loaded[0]
macros = loaded[1]
load_hotkeys(macros)

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
    [sg.Table(
        values=UpdateMid(cr),
        headings=curhead,
        num_rows=10,
        alternating_row_color='green',
        key='-cur-',
        enable_events=True,
        justification='center',
        visible=False,
        )],
    [
        sg.InputText(key="-crn-", size=(10, 20), visible=False),
        sg.Button(button_text='Hotkey', key='-htk-', visible=False),
        sg.T(htky, visible=False, key='-hts-'),
        sg.Submit(button_text="Create", key='-cre-', visible=False),
        sg.Button(button_text='Delete', key='-cdl-', visible=False),
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

# Updates the current macro page

# Resets all inputs
def Reset():
    window['-akmi-'].update('')
    window['-amm-'].update('Single')
    window['-mcb-'].update('-none-')
    window['-mcx-'].update('')
    window['-mcy-'].update('')
    window['-mmx-'].update('')
    window['-mmy-'].update('')

# Resets inputs of advanced mouse click
def ResetAdv():
    window['-mca-'].update('')
    window['-mct-'].update('')

# Toggles a boolean
def toggle(change):
    if change == True:
        change = False
    else:
        change = True
    return change

# Records a hotkey and returns it
def get_Hotkey():
    layout = [[sg.T('Currently listening for Hotkey...')],[sg.Button('Finished', key='-fin-')]]
    
    window = sg.Window('Hotkey', layout)
    keyboard.start_recording()

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case '-fin-':
                hotkey = ''
                temp = keyboard.stop_recording()
                for x in temp:
                    found = True
                    keys = hotkey.split('+')
                    for y in keys:
                        if y == convert(x):
                            found = False
                    if found and hotkey == '':
                        hotkey += convert(x)
                    elif found:
                        hotkey += '+'
                        hotkey += convert(x)
                break
    window.close()
    return hotkey

# Toggles the inputfields
def ToggleInp(x):
    for x in Inputs:
        x.update(disabled=x)

# ------ Event Loop ------
#   Window will check for user inputs and 
#   respond accordingly. Check for update
#   is passive
#   
#       event is the ID of the user input and 
#       values are the values for every component
#       in the window

Inputs = [window["-akmi-"],window["-mca-"],window["-mct-"],window["-mcx-"],window["-mcy-"],window["-mmx-"],window["-mmy-"],window["-crn-"]]
while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            if startup:
                enableStartup.setReg()
            saveStart(macros, startup)
            break
        case "-new-":
            window['-left-'].update(visible=True)
            window['-mid-'].update(visible=True)
        case "-cat-":
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
        case "-aca-":
            visible = toggle(visible)
            ResetAdv()
            window["-adv-"].update(visible=visible)
        case "-amm-":
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
        case "-am-":
            if values['-mmx-'] != '' and values['-mmy-'] != '':
                cr.append([0, int(values['-mmx-']), int(values['-mmy-'])])
                Reset()
                window['-cur-'].update(visible=True)
                window['-cur-'].update(values=UpdateMid(cr))
                window['-cre-'].update(visible=True)
                window['-crn-'].update(visible=True)
                window['-htk-'].update(visible=True)
                window['-hts-'].update(visible=True)
                window['-cdl-'].update(visible=True)
            else:
                messagebox.showerror('Warning', 'Please add values and retry')
        case "-ac-":
            if values['-mcx-'] != '' and values['-mcy-'] != '' and values['-mcb-'] != '':
                Reset()
                button = 0
                if values['-mcb-'] == 'Left':
                    button = 3
                elif values['-mcb-'] == 'Right':
                    button = 4
                elif values['-mcb-'] == 'Middle':
                    button = 5
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
                window['-cre-'].update(visible=True)
                window['-cur-'].update(values=UpdateMid(cr))
                window['-crn-'].update(visible=True)
                window['-htk-'].update(visible=True)
                window['-hts-'].update(visible=True)
                window['-cur-'].update(visible=True)
                window['-cdl-'].update(visible=True)
            else:
                messagebox.showerror('Warning', 'Please add values and retry')
        case '-ak-':
            Reset()
            if values['-amm-'] == 'Single':
                if sel != 'Nothing selected' and sel != '':
                    cr.append([2, [sel]])
                    window['-cur-'].update(visible=True)
                    window['-cur-'].update(values=UpdateMid(cr))
                    window['-cre-'].update(visible=True)
                    window['-crn-'].update(visible=True)
                    window['-htk-'].update(visible=True)
                    window['-hts-'].update(visible=True)
                    window['-cdl-'].update(visible=True)
                else:
                    messagebox.showerror('Warning', 'Please select a character and try again')
            elif values['-amm-'] == 'Multiple':
                if values['-akmi-'] != '':
                    cr.append([2, values['-akmi-']])
                    window['-cur-'].update(visible=True)
                    window['-cur-'].update(values=UpdateMid(cr))
                    window['-cre-'].update(visible=True)
                    window['-crn-'].update(visible=True)
                    window['-htk-'].update(visible=True)
                    window['-hts-'].update(visible=True)
                    window['-cdl-'].update(visible=True)
                else:
                    messagebox.showerror('Warning', 'Please enter a text and try again')
        case "-cre-":
            if values['-crn-'] != '':
                macros.append([values['-crn-'], htky, cr])
                keyboard.add_hotkey(htky, lambda x = len(macros) - 1: Run(macros[x]))
                cr = []
                view = "Nothing here yet"
                window['-crn-'].update('')
                window['-mac-'].update(values=macros)
                window['-cdl-'].update(visible=False)
                window['-cre-'].update(visible=False)
                window['-crn-'].update(visible=False)
                window['-htk-'].update(visible=False)
                window['-hts-'].update(visible=False)
                window['-cur-'].update(visible=False)
                window['-cur-'].update(values=UpdateMid(cr))
                window['-left-'].update(visible=False)
                window['-mid-'].update(visible=False)
            else:
                messagebox.showinfo('Provide a name', 'Please provide a name to the Macro')
        case '-cho-':
            sel = charSelector()
            window['-cho-'].update(sel)
        case '-del-':
            sel_mac = [macros[row] for row in values['-mac-']]
            try:
                macros.remove(sel_mac[0])
                keyboard.remove_hotkey(sel_mac[0][3])
            except:
                messagebox.showinfo('Warning', 'Select an entry to delete')
            window['-mac-'].update(values=macros)
        case '-run-':
            sel_mac = [macros[row] for row in values['-mac-']]
            try:
                Run(sel_mac[0])
            except:
                messagebox.showinfo('Warning', 'Select an entry to run')
        case '-htk-':
            ToggleInp(False)
            htky = ''
            htky = get_Hotkey()
            window['-hts-'].update(htky)
            ToggleInp(True)
        case '-lod-':
            loading = askopenfilename(filetypes=[("Macro files", "*.macros")])
            if loading != '':
                if macros != []:
                    keyboard.remove_all_hotkeys()
                macros = load(loading, macros)
                load_hotkeys(macros)
            window['-mac-'].update(values=macros)
        case '-sve-':
            save(macros)
        case '-cdl-':
            cr.remove(cr[values['-cur-'][0]])
            window['-cur-'].update(values=UpdateMid(cr))
window.close()