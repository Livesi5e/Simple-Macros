# An Application to program your own macros and use them globally
#
# Does not support recording

import PySimpleGUI as sg

# Inital variables

list = ("Mouse Movement", "Mouse Click", "Keyboard Input")
mb = ("Left", "Right")

# All window components

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
        sg.Submit(button_text="Add"),
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
        sg.Submit(button_text="Add"),
    ]
]

add_macro = [
    [
        sg.T("Input type: "),
        sg.Combo(values=list, size=(15, len(list)), default_value="Pick Input Type", key="-cat-", enable_events=True, readonly=True),
    ],
    [
        sg.pin(sg.Column(add_movement, key="-mousemove-", visible=False)),
        sg.pin(sg.Column(add_click, key="-mouseclick-", visible=False)),
    ],
]

new_macro = [
    [sg.Column(add_macro)],
]

# ------ Full layout ------

layout = [
    [
        sg.Column(new_macro),
        sg.VerticalSeparator(),
    ]
]

window = sg.Window("Simple Macros", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
    elif event == "-cat-":
        new_add = []
        combo = values["-cat-"]
        if combo == 'Mouse Movement':
            window["-mouseclick-"].update(visible=False)
            window["-mousemove-"].update(visible=True)
        if combo == 'Mouse Click':
            window["-mousemove-"].update(visible=False)
            window["-mouseclick-"].update(visible=True)
        if combo == 'Keyboard Input':
            window["-mousemove-"].update(visible=False)
            window["-mouseclick-"].update(visible=False)

window.close()