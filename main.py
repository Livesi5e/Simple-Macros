# An Application to program your own macros and use them globally
#
# Does not support macro recording

import PySimpleGUI as sg
from tkinter.filedialog import askopenfilename
import keyboard
from scripts.charSelect import charSelector
from scripts.DataManagement import load, save, saveStart, loadStart, loadOptions
from scripts.Conversion import convert, UpdateMid, UpdateList
from scripts.macros import Run, load_hotkeys
from scripts.OptionMenu import Options
from scripts.warning import warn

# ---- Inital variables ----

list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Middle", "Right")
amm = ("Single", "Multiple")
curhead=("ID", "     Type     ", "   X   ", "   Y   ", "   Key   ", "Clicks", "Time")
menu_list = ['File', ['Save', 'Load', 'New', '---', 'Options', '---', 'Exit']],['Edit', ['Run', 'Delete']]
cr = []
hotkeys = [] 
macros = []
active = []
htky = ''
sel=''
sel_mac = ''
view = "Nothing here yet"
font = ("Arial", 12)
visible = False
multiple = False
single = True

# ------ Startup ------

prefs = loadOptions()
if prefs[1]:
    loaded = loadStart()
    macros, active = loaded[0], loaded[1]
    load_hotkeys(macros, True, active)

# - All window components -

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
        sg.Button(button_text='Cancel', key='-can-', visible=False),
    ]
]

your_macros = [
    [
        sg.Table(
            values=UpdateList(macros, active),
            headings=['Macros', 'Hotkey', 'Active'],
            num_rows=10,
            alternating_row_color='green',
            key='-mac-',
            enable_events=True,
            justification='center',
        )
    ],
    [sg.Button(button_text='New', key='-new-'), sg.Button(button_text='Delete', key='-del-'), sg.Button(button_text='Load', key='-lod-'), sg.Button(button_text='Save', key='-sve-'), sg.Button(button_text='Active', key='-off-')]
]

# ------ Full layout ------

layout = [
    [sg.Menu(menu_list)],
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

def New():
    global macros
    if macros != []:
        keyboard.remove_all_hotkeys()
    macros = []

def saveNew():
    save(macros, active)
    New()

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
            if prefs[1]:
                saveStart(macros, active)
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
                cr.append([0, int(values['-mmx-']), int(values['-mmy-']), len(cr)])
                Reset()
                window['-cur-'].update(visible=True)
                window['-cur-'].update(values=UpdateMid(cr))
                window['-cre-'].update(visible=True)
                window['-crn-'].update(visible=True)
                window['-htk-'].update(visible=True)
                window['-hts-'].update(visible=True)
                window['-cdl-'].update(visible=True)
                window['-can-'].update(visible=True)
            else:
                warn('Warning', 'Please add values and retry', Okay=lambda : None)
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
                cr.append([1, button, int(values['-mcx-']), int(values['-mcy-']), amt, time, len(cr)])
                window['-cre-'].update(visible=True)
                window['-cur-'].update(values=UpdateMid(cr))
                window['-crn-'].update(visible=True)
                window['-htk-'].update(visible=True)
                window['-hts-'].update(visible=True)
                window['-cur-'].update(visible=True)
                window['-cdl-'].update(visible=True)
                window['-can-'].update(visible=True)
            else:
                warn('Warning', 'Please add values and retry', Okay=lambda : None)
        case '-ak-':
            Reset()
            if values['-amm-'] == 'Single':
                if sel != 'Nothing selected' and sel != '':
                    cr.append([2, [sel], len(cr)])
                    window['-cur-'].update(visible=True)
                    window['-cur-'].update(values=UpdateMid(cr))
                    window['-cre-'].update(visible=True)
                    window['-crn-'].update(visible=True)
                    window['-htk-'].update(visible=True)
                    window['-hts-'].update(visible=True)
                    window['-cdl-'].update(visible=True)
                    window['-can-'].update(visible=True)
                else:
                    warn('Warning', 'Please select a character and try again', Okay=lambda : None)
            elif values['-amm-'] == 'Multiple':
                if values['-akmi-'] != '':
                    cr.append([2, values['-akmi-'], len(cr)])
                    window['-cur-'].update(visible=True)
                    window['-cur-'].update(values=UpdateMid(cr))
                    window['-cre-'].update(visible=True)
                    window['-crn-'].update(visible=True)
                    window['-htk-'].update(visible=True)
                    window['-hts-'].update(visible=True)
                    window['-cdl-'].update(visible=True)
                    window['-can-'].update(visible=True)
                else:
                    warn('Warning', 'Please enter a text and try again', Okay=lambda : None)
        case "-cre-":
            if values['-crn-'] != '' and htky != '':
                macros.append([values['-crn-'], htky, cr])
                active.append(True)
                keyboard.add_hotkey(htky, lambda x = len(macros) - 1: Run(macros[x]))
                cr = []
                view = "Nothing here yet"
                window['-crn-'].update('')
                window['-mac-'].update(values=UpdateList(macros, active))
                window['-cdl-'].update(visible=False)
                window['-cre-'].update(visible=False)
                window['-crn-'].update(visible=False)
                window['-htk-'].update(visible=False)
                window['-hts-'].update(visible=False)
                window['-cur-'].update(visible=False)
                window['-cur-'].update(values=UpdateMid(cr))
                window['-left-'].update(visible=False)
                window['-mid-'].update(visible=False)
                window['-can-'].update(visible=False)
            elif htky != '':
                warn('Provide a name', 'Please provide a name to the Macro', Okay=lambda : None)
            else:
                warn('Provide a Hotkey', 'Please provide a hotkey to the Macro', Okay=lambda : None)
        case '-cho-':
            sel = charSelector()
            window['-cho-'].update(sel)
        case '-del-':
            sel_mac = [macros[row] for row in values['-mac-']]
            try:
                macros.remove(sel_mac[0])
                load_hotkeys(macros, False, active)
            except:
                warn('Attention!','Select an entry to delete', Okay=lambda : None)
            window['-mac-'].update(values=UpdateList(macros, active))
        case '-run-':
            sel_mac = [macros[row] for row in values['-mac-']]
            try:
                Run(sel_mac[0])
            except:
                warn('Attention!','Select an entry to run', Okay=lambda : None)
        case '-htk-':
            ToggleInp(False)
            htky = ''
            htky = get_Hotkey()
            window['-hts-'].update(htky)
            ToggleInp(True)
        case '-lod-':
            loading = askopenfilename(filetypes=[("Macro files", "*.macros")])
            if loading != '':
                temp = load(loading, macros)
                if macros != []:
                    tempmac = False
                else:
                    tempmac = True
                macros, active = temp[0], temp[1]
                load_hotkeys(macros, tempmac, active)
            window['-mac-'].update(values=UpdateList(macros, active))
        case '-sve-':
            save(macros, active)
        case '-cdl-':
            cr.remove(cr[values['-cur-'][0]])
            window['-cur-'].update(values=UpdateMid(cr))
        case '-can-':
            cr = []
            Reset()
            ResetAdv()
            window['-crn-'].update('')
            window['-mac-'].update(values=UpdateList(macros, active))
            window['-cdl-'].update(visible=False)
            window['-cre-'].update(visible=False)
            window['-crn-'].update(visible=False)
            window['-htk-'].update(visible=False)
            window['-hts-'].update(visible=False)
            window['-cur-'].update(visible=False)
            window['-cur-'].update(values=UpdateMid(cr))
            window['-left-'].update(visible=False)
            window['-mid-'].update(visible=False)
            window['-can-'].update(visible=False)
        case '-off-':
            sel_mac = [active[row] for row in values['-mac-']]
            # try:
            sel_mac[0] = toggle(sel_mac[0])
            for x in active:
                if x:
                    tempmac = False
            active[values['-mac-'][0]] = sel_mac[0]
            tempmac = True
            load_hotkeys(macros, tempmac, active)
            window['-mac-'].update(values=UpdateList(macros, active))
            # except:
            #     warn('Warning!', 'Select an entry to toggle on or off!', Okay=lambda : None)
        case 'Save':
            save(macros, active)
        case 'Load':
            loading = askopenfilename(filetypes=[("Macro files", "*.macros")])
            if loading != '':
                temp = load(loading, macros)
                if macros != []:
                    tempmac = False
                else:
                    tempmac = True
                macros, active = temp[0], temp[1]
                load_hotkeys(macros, tempmac, active)
            window['-mac-'].update(values=UpdateList(macros, active))
        case 'Options':
            Options(loadOptions())
        case 'New':
            warn('Warning!','Attention! This will delete all your current macros.\nDo you want to save them before proceeding?', Yes=saveNew, No=New)
            window['-mac-'].update(values=UpdateList(macros, active))
        case 'Run':
            sel_mac = [macros[row] for row in values['-mac-']]
            try:
                Run(sel_mac[0])
            except:
                warn('Attention!','Select an entry to run', Okay=lambda : None)
        case 'Delete':
            sel_mac = [macros[row] for row in values['-mac-']]
            try:
                macros.remove(sel_mac[0])
                load_hotkeys(macros, False, active)
            except:
                warn('Attention!','Select an entry to delete', Okay=lambda : None)
            window['-mac-'].update(values=UpdateList(macros, active))
        case 'Exit':
            if prefs[1]:
                saveStart(macros, active)
            break

window.close()