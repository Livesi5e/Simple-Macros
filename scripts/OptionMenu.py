import PySimpleGUI as sg
# from enableStartup import setReg

def Options():
    
    # All window components

    checks = [
        [sg.Checkbox('', default=False)],
        [sg.Checkbox('', default=False)]
    ]

    texts = [
        [sg.T('Auto Save')],
        [sg.T('Auto Load')]
    ]

    options = [
        [sg.pin(sg.Column(texts)), sg.pin(sg.Column(checks))]
    ]

    # ------ Full layout ------

    layout = [
        [sg.pin(sg.Frame('',options))],
    ]

    window = sg.Window('Options', layout)

    # ------ Event Loop ------

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break

    window.close()