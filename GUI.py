import PySimpleGUI as psg


def reglog():
    layout = psg.Column ([[psg.Text('User Login Name:')], [psg.Input(size=(20, 1), key='--NAME--')], [psg.Text('User Password:')], [psg.Input(size=(20, 1), key='--PASSWORD--')], [psg.Button('Registration')]],
        [[psg.Text('Login Name:')], [psg.Input(size=(20, 1), key='--NAME--')], [psg.Text('Password:')], [psg.Input(size=(20, 1), key='--PASSWORD--')], [psg.Button('Log In')]],pad=(0,0))
    window = psg.Window('Reg and Log In', layout, size=(800,600))
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == 'Quit':
            break
    window.close()


reglog()
