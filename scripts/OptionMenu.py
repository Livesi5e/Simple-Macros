import PySimpleGUI as sg
from enableStartup import enableReg, disableReg

def Options():
    
    # All window components

    checks = [
        [sg.Checkbox('', default=False, key='-ats-')],
        [sg.Checkbox('', default=False, key='-atl-')]
    ]

    texts = [
        [sg.T('Auto Start')],
        [sg.T('Auto Load')]
    ]

    options = [
        [sg.pin(sg.Column(texts)), sg.pin(sg.Column(checks))]
    ]

    # ------ Full layout ------

    layout = [
        [sg.pin(sg.Frame('',options))],
        [sg.Button('Apply', key='-app-')]
    ]

    window = sg.Window('Options', layout)

    # ------ Event Loop ------

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
        if values['-ats-'] == True:
            enableReg()
        if values['-atl-'] == True:
            print('true')

    window.close()