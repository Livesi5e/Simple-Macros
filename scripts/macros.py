import keyboard
import pyautogui as pag

# Executes a macro based on the array input
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

def load_hotkeys(macros, startup):
    i = 0
    if startup != True:
        keyboard.remove_all_hotkeys()
    for x in macros:
        keyboard.add_hotkey(x[1], lambda x = i: Run(macros[x]))
