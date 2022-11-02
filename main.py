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

# Inital variables

list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Middle", "Right")
amm = ("Single", "Multiple")
cr = []
htky = ''
hotkeys = []
macros = []
bindings = []
id = 0
sel=''
sel_mac = ''
view = "Nothing here yet"
font = ("Arial", 12)
visible = False
multiple = False
single = True
save = ''

print(pag.KEYBOARD_KEYS)

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
                print(x[1])
                pag.typewrite(x[1])
            case _:
                print('NaN')

def get_Hotkey():
    temp = keyboard.read_hotkey()
    return temp

def char_select():
    sim = True
    chosen = 'Nothing selected'
    categories = ('Function Keys', 'Control Keys', 'Numpad')
    chars = [
        [
            sg.Button(button_text='a', button_color='NavyBlue', size=(2, 1), key='-a-'), 
            sg.Button(button_text='b', button_color='NavyBlue', size=(2, 1), key='-b-'),
            sg.Button(button_text='c', button_color='NavyBlue', size=(2, 1), key='-c-'),
            sg.Button(button_text='d', button_color='NavyBlue', size=(2, 1), key='-d-'),
            sg.Button(button_text='e', button_color='NavyBlue', size=(2, 1), key='-e-'),
            sg.Button(button_text='f', button_color='NavyBlue', size=(2, 1), key='-f-'),
            sg.Button(button_text='g', button_color='NavyBlue', size=(2, 1), key='-g-'),
            sg.Button(button_text='h', button_color='NavyBlue', size=(2, 1), key='-h-'),
            sg.Button(button_text='i', button_color='NavyBlue', size=(2, 1), key='-i-'),
        ],
        [
            sg.Button(button_text='j', button_color='NavyBlue', size=(2, 1), key='-j-'), 
            sg.Button(button_text='k', button_color='NavyBlue', size=(2, 1), key='-k-'),
            sg.Button(button_text='l', button_color='NavyBlue', size=(2, 1), key='-l-'),
            sg.Button(button_text='m', button_color='NavyBlue', size=(2, 1), key='-m-'),
            sg.Button(button_text='n', button_color='NavyBlue', size=(2, 1), key='-n-'),
            sg.Button(button_text='o', button_color='NavyBlue', size=(2, 1), key='-o-'),
            sg.Button(button_text='p', button_color='NavyBlue', size=(2, 1), key='-p-'),
            sg.Button(button_text='q', button_color='NavyBlue', size=(2, 1), key='-q-'),
            sg.Button(button_text='r', button_color='NavyBlue', size=(2, 1), key='-r-'),
        ],
        [
            sg.Button(button_text='s', button_color='NavyBlue', size=(2, 1), key='-s-'), 
            sg.Button(button_text='t', button_color='NavyBlue', size=(2, 1), key='-t-'),
            sg.Button(button_text='u', button_color='NavyBlue', size=(2, 1), key='-u-'),
            sg.Button(button_text='v', button_color='NavyBlue', size=(2, 1), key='-v-'),
            sg.Button(button_text='w', button_color='NavyBlue', size=(2, 1), key='-w-'),
            sg.Button(button_text='x', button_color='NavyBlue', size=(2, 1), key='-x-'),
            sg.Button(button_text='y', button_color='NavyBlue', size=(2, 1), key='-y-'),
            sg.Button(button_text='z', button_color='NavyBlue', size=(2, 1), key='-z-'),
            sg.Button(button_text='0', button_color='NavyBlue', size=(2, 1), key='-0-'),
        ],
        [
            sg.Button(button_text='1', button_color='NavyBlue', size=(2, 1), key='-1-'), 
            sg.Button(button_text='2', button_color='NavyBlue', size=(2, 1), key='-2-'),
            sg.Button(button_text='3', button_color='NavyBlue', size=(2, 1), key='-3-'),
            sg.Button(button_text='4', button_color='NavyBlue', size=(2, 1), key='-4-'),
            sg.Button(button_text='5', button_color='NavyBlue', size=(2, 1), key='-5-'),
            sg.Button(button_text='6', button_color='NavyBlue', size=(2, 1), key='-6-'),
            sg.Button(button_text="7", button_color='NavyBlue', size=(2, 1), key='-7-'),
            sg.Button(button_text='8', button_color='NavyBlue', size=(2, 1), key='-8-'),
            sg.Button(button_text='9', button_color='NavyBlue', size=(2, 1), key='-9-'),
        ],
        [
            sg.Button(button_text='!', button_color='NavyBlue', size=(2, 1), key='-!-'), 
            sg.Button(button_text='"', button_color='NavyBlue', size=(2, 1), key='-"-'),
            sg.Button(button_text='#', button_color='NavyBlue', size=(2, 1), key='-#-'),
            sg.Button(button_text='$', button_color='NavyBlue', size=(2, 1), key='-$-'),
            sg.Button(button_text='%', button_color='NavyBlue', size=(2, 1), key='-%-'),
            sg.Button(button_text='&', button_color='NavyBlue', size=(2, 1), key='-&-'),
            sg.Button(button_text="'", button_color='NavyBlue', size=(2, 1), key="-'-"),
            sg.Button(button_text='(', button_color='NavyBlue', size=(2, 1), key='-(-'),
            sg.Button(button_text=')', button_color='NavyBlue', size=(2, 1), key='-)-'),
        ],
        [
            sg.Button(button_text='*', button_color='NavyBlue', size=(2, 1), key='-*-'), 
            sg.Button(button_text='+', button_color='NavyBlue', size=(2, 1), key='-+-'),
            sg.Button(button_text=',', button_color='NavyBlue', size=(2, 1), key='-,-'),
            sg.Button(button_text='-', button_color='NavyBlue', size=(2, 1), key='---'),
            sg.Button(button_text='.', button_color='NavyBlue', size=(2, 1), key='-.-'),
            sg.Button(button_text='/', button_color='NavyBlue', size=(2, 1), key='-/-'),
            sg.Button(button_text=":", button_color='NavyBlue', size=(2, 1), key='-:-'),
            sg.Button(button_text=';', button_color='NavyBlue', size=(2, 1), key='-;-'),
            sg.Button(button_text='<', button_color='NavyBlue', size=(2, 1), key='-<-'),
        ],
        [
            sg.Button(button_text='=', button_color='NavyBlue', size=(2, 1), key='-=-'), 
            sg.Button(button_text='>', button_color='NavyBlue', size=(2, 1), key='->-'),
            sg.Button(button_text='?', button_color='NavyBlue', size=(2, 1), key='-?-'),
            sg.Button(button_text='@', button_color='NavyBlue', size=(2, 1), key='-@-'),
            sg.Button(button_text='[', button_color='NavyBlue', size=(2, 1), key='-[-'),
            sg.Button(button_text=']', button_color='NavyBlue', size=(2, 1), key='-]-'),
            sg.Button(button_text="^", button_color='NavyBlue', size=(2, 1), key='-^-'),
            sg.Button(button_text='_', button_color='NavyBlue', size=(2, 1), key='-_-'),
            sg.Button(button_text='`', button_color='NavyBlue', size=(2, 1), key='-`-'),
        ],
        [
            sg.Button(button_text='{', button_color='NavyBlue', size=(2, 1), key='-{-'), 
            sg.Button(button_text='|', button_color='NavyBlue', size=(2, 1), key='-|-'),
            sg.Button(button_text='}', button_color='NavyBlue', size=(2, 1), key='-}-'),
            sg.Button(button_text='~', button_color='NavyBlue', size=(2, 1), key='-~-'),
            sg.Button(button_text='Enter', button_color='NavyBlue', size=(4, 1), key='-ent-'), 
            sg.Button(button_text='Space', button_color='NavyBlue', size=(5, 1), key='-spa-'),
            sg.Button(button_text='Control', button_color='NavyBlue', size=(6, 1), key='-crl-'),
        ],
        [
            sg.Button(button_text='Alt', button_color='NavyBlue', size=(4, 1), key='-alt-'),
            sg.Button(button_text='Tab', button_color='NavyBlue', size=(4, 1), key='-tab-'),
        ],
    ]
    func_keys=[
        [
            sg.Button(button_text='F1', button_color='NavyBlue', size=(2, 1), key='-F1-'), 
            sg.Button(button_text='F2', button_color='NavyBlue', size=(2, 1), key='-F2-'),
            sg.Button(button_text='F3', button_color='NavyBlue', size=(2, 1), key='-F3-'),
            sg.Button(button_text='F4', button_color='NavyBlue', size=(2, 1), key='-F4-'),
            sg.Button(button_text='F5', button_color='NavyBlue', size=(2, 1), key='-F5-'),
            sg.Button(button_text='F6', button_color='NavyBlue', size=(2, 1), key='-F6-'),
            sg.Button(button_text="F7", button_color='NavyBlue', size=(2, 1), key='-F7-'),
            sg.Button(button_text='F8', button_color='NavyBlue', size=(2, 1), key='-F8-'),
            sg.Button(button_text='F9', button_color='NavyBlue', size=(2, 1), key='-F9-'),
        ],
        [
            sg.Button(button_text='F10', button_color='NavyBlue', size=(4, 1), key='-F10-'),
            sg.Button(button_text='F11', button_color='NavyBlue', size=(4, 1), key='-F11-'),
            sg.Button(button_text='F12', button_color='NavyBlue', size=(4, 1), key='-F12-'),
            sg.Button(button_text='F13', button_color='NavyBlue', size=(4, 1), key='-F13-'),
            sg.Button(button_text='F14', button_color='NavyBlue', size=(4, 1), key='-F14-'),
            sg.Button(button_text='F15', button_color='NavyBlue', size=(4, 1), key='-F15-'),
        ],
        [
            sg.Button(button_text='F16', button_color='NavyBlue', size=(4, 1), key='-F16-'),
            sg.Button(button_text='F17', button_color='NavyBlue', size=(4, 1), key='-F17-'),
            sg.Button(button_text='F18', button_color='NavyBlue', size=(4, 1), key='-F18-'),
            sg.Button(button_text='F19', button_color='NavyBlue', size=(4, 1), key='-F19-'),
            sg.Button(button_text='F20', button_color='NavyBlue', size=(4, 1), key='-F20-'),
            sg.Button(button_text='F21', button_color='NavyBlue', size=(4, 1), key='-F21-'),
        ],
        [
            sg.Button(button_text='F22', button_color='NavyBlue', size=(4, 1), key='-F22-'),
            sg.Button(button_text='F23', button_color='NavyBlue', size=(4, 1), key='-F23-'),
            sg.Button(button_text='F24', button_color='NavyBlue', size=(4, 1), key='-F24-'),
        ]
    ]
    crtl_keys = [
        [
            sg.Button(button_text='accept', button_color='NavyBlue', size=(5, 1)),
            sg.Button(button_text='add', button_color='NavyBlue', size=(4, 1)),
            sg.Button(button_text='alt', button_color='NavyBlue', size=(4, 1)),
            sg.Button(button_text='altleft', button_color='NavyBlue', size=(5, 1)),
            sg.Button(button_text='altright', button_color='NavyBlue', size=(5, 1)),
        ],
        [
            sg.Button(button_text='backspace', button_color='NavyBlue', size=(8, 1)),
            sg.Button(button_text='browserback', button_color='NavyBlue', size=(9, 1)),
            sg.Button(button_text='browserfavorites', button_color='NavyBlue', size=(11, 1)),
        ],
        [
            sg.Button(button_text='browserforward', button_color='NavyBlue', size=(10, 1)),
            sg.Button(button_text='browserhome', button_color='NavyBlue', size=(9, 1)),
            sg.Button(button_text='browserrefresh', button_color='NavyBlue', size=(10, 1)),
        ],
        [
            sg.Button(button_text='browsersearch', button_color='NavyBlue', size=(10, 1)),
            sg.Button(button_text='browsertop', button_color='NavyBlue', size=(8, 1)),
            sg.Button(button_text='browsersearch', button_color='NavyBlue', size=(10, 1)),
        ]
]
    selector = [[sg.Combo(default_value='Function Keys', size=(15, 5), readonly=True, values=categories, enable_events=True, key='-slc-')]]
    layout = [
        [sg.pin(sg.Column(selector, visible=False, key='-sel-'))],
        [sg.pin(sg.Column(chars, size=(320, 140), scrollable=True, vertical_scroll_only=True, visible=True, key='-sim-'))],
        [sg.pin(sg.Column(func_keys, size=(320, 140), scrollable=True, vertical_scroll_only=True, visible=False, key='-fun-'))],
        [sg.pin(sg.Column(crtl_keys, size=(320, 140), scrollable=True, vertical_scroll_only=True, visible=False, key='-crt-'))],
        [sg.T("Selected:"), sg.T(chosen, key='-sho-')],
        [sg.Button(button_text='Select', key='Exit'), sg.Button(button_text='Special Inputs', key='-spe-')]
    ]
    window = sg.Window('Char Selector', layout)
    while True:
        event, values = window.read()
        match event:
            case 'Exit':
                break
            case sg.WIN_CLOSED:
                break
            case '-spe-':            
                if sim == True:
                    sim = False
                    window['-sim-'].update(visible=False)
                    window['-sel-'].update(visible=True)
                    window['-fun-'].update(visible=True)
                else:
                    sim = True
                    window['-sim-'].update(visible=True)
                    window['-sel-'].update(visible=False)
                    window['-fun-'].update(visible=False)
            case '-slc-':
                print(f'{values["-slc-"]=}')
                if values['-slc-'] == 'Function Keys':
                    window['-crt-'].update(visible=False)
                    window['-fun-'].update(visible=True)
                elif values['-slc-'] == 'Control Keys':
                    window['-fun-'].update(visible=False)
                    window['-crt-'].update(visible=True)
            case '-a-':
                chosen = 'a'
                window['-sho-'].update(chosen)
            case '-b-':
                chosen = 'b'
                window['-sho-'].update(chosen)
            case '-c-':
                chosen = 'c'
                window['-sho-'].update(chosen)
            case '-d-':
                chosen = 'd'
                window['-sho-'].update(chosen)
            case '-e-':
                chosen = 'e'
                window['-sho-'].update(chosen)
            case '-f-':
                chosen = 'f'
                window['-sho-'].update(chosen)
            case '-g-':
                chosen = 'g'
                window['-sho-'].update(chosen)
            case '-h-':
                chosen = 'h'
                window['-sho-'].update(chosen)
            case '-i-':
                chosen = 'i'
                window['-sho-'].update(chosen)
            case '-j-':
                chosen = 'j'
                window['-sho-'].update(chosen)
            case '-k-':
                chosen = 'k'
                window['-sho-'].update(chosen)
            case '-l-':
                chosen = 'l'
                window['-sho-'].update(chosen)
            case '-m-':
                chosen = 'm'
                window['-sho-'].update(chosen)
            case '-n-':
                chosen = 'n'
                window['-sho-'].update(chosen)
            case '-o-':
                chosen = 'o'
                window['-sho-'].update(chosen)
            case '-p-':
                chosen = 'p'
                window['-sho-'].update(chosen)
            case '-q-':
                chosen = 'q'
                window['-sho-'].update(chosen)
            case '-r-':
                chosen = 'r'
                window['-sho-'].update(chosen)
            case '-s-':
                chosen = 's'
                window['-sho-'].update(chosen)
            case '-t-':
                chosen = 't'
                window['-sho-'].update(chosen)
            case '-u-':
                chosen = 'u'
                window['-sho-'].update(chosen)
            case '-v-':
                chosen = 'v'
                window['-sho-'].update(chosen)
            case '-w-':
                chosen = 'w'
                window['-sho-'].update(chosen)
            case '-x-':
                chosen = 'x'
                window['-sho-'].update(chosen)
            case '-y-':
                chosen = 'y'
                window['-sho-'].update(chosen)
            case '-z-':
                chosen = 'z'
                window['-sho-'].update(chosen)
            case '-0-':
                chosen = '0'
                window['-sho-'].update(chosen)
            case '-1-':
                chosen = '1'
                window['-sho-'].update(chosen)
            case '-2-':
                chosen = '2'
                window['-sho-'].update(chosen)
            case '-3-':
                chosen = '3'
                window['-sho-'].update(chosen)
            case '-4-':
                chosen = '4'
                window['-sho-'].update(chosen)
            case '-5-':
                chosen = '5'
                window['-sho-'].update(chosen)
            case '-6-':
                chosen = '6'
                window['-sho-'].update(chosen)
            case '-7-':
                chosen = '7'
                window['-sho-'].update(chosen)
            case '-8-':
                chosen = '8'
                window['-sho-'].update(chosen)
            case '-9-':
                chosen = '9'
                window['-sho-'].update(chosen)
            case '-!-':
                chosen = '!'
                window['-sho-'].update(chosen)
            case '-"-':
                chosen = '"'
                window['-sho-'].update(chosen)
            case '-#-':
                chosen = '#'
                window['-sho-'].update(chosen)
            case '-$-':
                chosen = '$'
                window['-sho-'].update(chosen)
            case '-%-':
                chosen = '%'
                window['-sho-'].update(chosen)
            case '-&-':
                chosen = '&'
                window['-sho-'].update(chosen)
            case "-'-":
                chosen = "'"
                window['-sho-'].update(chosen)
            case '-(-':
                chosen = '('
                window['-sho-'].update(chosen)
            case '-)-':
                chosen = ')'
                window['-sho-'].update(chosen)
            case '-*-':
                chosen = '*'
                window['-sho-'].update(chosen)
            case '-+-':
                chosen = '+'
                window['-sho-'].update(chosen)
            case '-,-':
                chosen = ','
                window['-sho-'].update(chosen)
            case '---':
                chosen = '-'
                window['-sho-'].update(chosen)
            case '-.-':
                chosen = '.'
                window['-sho-'].update(chosen)
            case '-/-':
                chosen = '/'
                window['-sho-'].update(chosen)
            case '-:-':
                chosen = ':'
                window['-sho-'].update(chosen)
            case '-;-':
                chosen = ';'
                window['-sho-'].update(chosen)
            case '-<-':
                chosen = '<'
                window['-sho-'].update(chosen)
            case '-=-':
                chosen = '='
                window['-sho-'].update(chosen)
            case '->-':
                chosen = '>'
                window['-sho-'].update(chosen)
            case '-?-':
                chosen = '?'
                window['-sho-'].update(chosen)
            case '-@-':
                chosen = '@'
                window['-sho-'].update(chosen)
            case '-[-':
                chosen = '['
                window['-sho-'].update(chosen)
            case '-]-':
                chosen = ']'
                window['-sho-'].update(chosen)
            case '-^-':
                chosen = '^'
                window['-sho-'].update(chosen)
            case '-_-':
                chosen = '_'
                window['-sho-'].update(chosen)
            case '-`-':
                chosen = '`'
                window['-sho-'].update(chosen)
            case '-{-':
                chosen = '{'
                window['-sho-'].update(chosen)
            case '-|-':
                chosen = '|'
                window['-sho-'].update(chosen)
            case '-}-':
                chosen = '}'
                window['-sho-'].update(chosen)
            case '-~-':
                chosen = '~'
                window['-sho-'].update(chosen)
            case '-new-':
                chosen = '\\n'
                window['-sho-'].update(chosen)
            case '-rew-':
                chosen = '\\r'
                window['-sho-'].update(chosen)
            case '-bac-':
                chosen = '\\\\'
                window['-sho-'].update(chosen)
            case '-spc-':
                chosen = ' '
                window['-sho-'].update(chosen)
            case '-F1-':
                chosen = 'F1'
                window['-sho-'].update(chosen)
            case '-F2-':
                chosen = 'F2'
                window['-sho-'].update(chosen)
            case '-F3-':
                chosen = 'F3'
                window['-sho-'].update(chosen)
            case '-F4-':
                chosen = 'F4'
                window['-sho-'].update(chosen)
            case '-F5-':
                chosen = 'F5'
                window['-sho-'].update(chosen)
            case '-F6-':
                chosen = 'F6'
                window['-sho-'].update(chosen)
            case '-F7-':
                chosen = 'F7'
                window['-sho-'].update(chosen)
            case '-F8-':
                chosen = 'F8'
                window['-sho-'].update(chosen)
            case '-F9-':
                chosen = 'F9'
                window['-sho-'].update(chosen)
            case '-F10-':
                chosen = 'F10'
                window['-sho-'].update(chosen)
            case '-F11-':
                chosen = 'F11'
                window['-sho-'].update(chosen)
            case '-F12-':
                chosen = 'F12'
                window['-sho-'].update(chosen)
            case '-F13-':
                chosen = 'F13'
                window['-sho-'].update(chosen)
            case '-F14-':
                chosen = 'F14'
                window['-sho-'].update(chosen)
            case '-F15-':
                chosen = 'F15'
                window['-sho-'].update(chosen)
            case '-F16-':
                chosen = 'F16'
                window['-sho-'].update(chosen)
            case '-F17-':
                chosen = 'F17'
                window['-sho-'].update(chosen)
            case '-F18-':
                chosen = 'F18'
                window['-sho-'].update(chosen)
            case '-F19-':
                chosen = 'F19'
                window['-sho-'].update(chosen)
            case '-F20-':
                chosen = 'F20'
                window['-sho-'].update(chosen)
            case '-F21-':
                chosen = 'F21'
                window['-sho-'].update(chosen)
            case '-F22-':
                chosen = 'F22'
                window['-sho-'].update(chosen)
            case '-F23-':
                chosen = 'F23'
                window['-sho-'].update(chosen)
            case '-F24-':
                chosen = 'F24'
                window['-sho-'].update(chosen)
            case '-spa-':
                chosen = ' '
                window['-sho-'].update(chosen)
            case '-ent-':
                chosen = 'enter'
                window['-sho-'].update(chosen)
            case '-crl-':
                chosen = 'crtl'
                window['-sho-'].update(chosen)
            case '-alt-':
                chosen = 'alt'
                window['-sho-'].update(chosen)
            case '-tab-':
                chosen = 'tab'
                window['-sho-'].update(chosen)
    window.close()
    if chosen != 'Nothing selected':
        return chosen
    else:
        return ''

# ------ Event Loop ------

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
            macros.append([values['-crn-'], htky, cr, htky])
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
        sel = char_select()
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