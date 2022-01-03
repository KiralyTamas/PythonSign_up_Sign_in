import PySimpleGUI as psg
from PySimpleGUI import VerticalSeparator


def reglog():
    layout1 = [psg.Column([[psg.Text('User Login Name:')], [psg.Input(size=(20, 1), key='--NAME--')], [psg.Text('User Password:')], [psg.Input(size=(20, 1), key='--PASSWORD--')], [psg.Button('Registration')]], element_justification='center',pad=(0,0))]
    vertical=VerticalSeparator()
    layout2=[psg.Column([[psg.Text('Login Name:')], [psg.Input(size=(20, 1), key='--NAME--')], [psg.Text('Password:')], [psg.Input(size=(20, 1), key='--PASSWORD--')], [psg.Button('Log In')]], element_justification='center', pad=(0,0))]
    layout=[layout1,vertical,layout2]
    window = psg.Window('Reg and Log In', layout)
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == 'Quit':
            break
    window.close()


reglog()
