import PySimpleGUI as sg

# This Function generates a warning window.
# 
#   Syntax:
#   warn(title, message, button1_name=function, button2_name=function, ...)
#
#   You can use anonymous functions with lambda

def warn(title, message, **param):
    sg.theme('LightBlue2')
    buttons = [[]]

    for name, func in param.items():
        buttons[0].append(sg.Button(str(name), key=str(name)))

    layout = [[sg.T(message)],[sg.pin(sg.Column(buttons))]]

    window = sg.Window(title, layout)
    
    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
        for name, func in param.items():
            if event == str(name):
                window.close()
                func()

    window.close() 