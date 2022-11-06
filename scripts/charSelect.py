# A collection of all functions
# surrounding character selection

import PySimpleGUI as sg
import pyautogui as pag

print(pag.KEYBOARD_KEYS)

# ------ Importable Functions ------

def charSelector():
    # Opens a new Window in which
    # the user can select a char 
    # to return
    #
    # Initial variables

    sim = True
    chosen = 'Nothing selected'
    categories = ('Function Keys', 'Control Keys', 'Numpad')

    # All window components

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
        ],
        [            
            sg.Button(button_text='capslock', button_color='NavyBlue', size=(7, 1)),
            sg.Button(button_text='browsersearch', button_color='NavyBlue', size=(10, 1)),
        ]
    ]

    selector = [[sg.Combo(default_value='Function Keys', size=(15, 5), readonly=True, values=categories, enable_events=True, key='-slc-')]]

    # ------ Full layout ------

    layout = [
        [sg.pin(sg.Column(selector, visible=False, key='-sel-'))],
        [sg.pin(sg.Column(chars, size=(320, 140), scrollable=True, vertical_scroll_only=True, visible=True, key='-sim-'))],
        [sg.pin(sg.Column(func_keys, size=(320, 140), scrollable=True, vertical_scroll_only=True, visible=False, key='-fun-'))],
        [sg.pin(sg.Column(crtl_keys, size=(320, 140), scrollable=True, vertical_scroll_only=True, visible=False, key='-crt-'))],
        [sg.T("Selected:"), sg.T(chosen, key='-sho-')],
        [sg.Button(button_text='Select', key='Exit'), sg.Button(button_text='Special Inputs', key='-spe-')]
    ]


    window = sg.Window('Char Selector', layout)

    # ------ Functions ------

    def getChar():
        print('test')

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

    # ------ Event Loop ------
    #   Window will be closed, value will be returned and script ends

    window.close()
    if chosen != 'Nothing selected':
        return chosen
    else:
        return ''

# ------ Test code ------

test = charSelector()