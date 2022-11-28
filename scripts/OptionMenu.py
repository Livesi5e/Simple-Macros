import PySimpleGUI as sg
from enableStartup import enableReg, disableReg
from scripts.DataManagement import saveOptions

def Options(state):
    # ----- Variables -----

    save = []

    # ----- Load Save -----

    if state[0] == 0:
        save.append(False)
    else:
        save.append(True)
    if state[1] == 0:
        save.append(False)
    else:
        save.append(True)

    # All window components

    checks = [
        [sg.Checkbox('', default=save[0], key='-ats-')],
        [sg.Checkbox('', default=save[1], key='-atl-')]
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
        [sg.Button('Apply', key='-app-'), sg.Button('Close', key='-cls-')]
    ]

    window = sg.Window('Options', layout)

    # ------ Event Loop ------

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case '-cls-':
                break
        if values['-ats-'] == True:
            enableReg()
        else:
            disableReg()
        saveOptions(values['-ats-'], values['-atl-'])

    window.close()