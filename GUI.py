import PySimpleGUI as sg


def reglog():
    register = [[sg.Frame('Registration',[[sg.Text('User Login Name:')],[sg.Input(size=(20, 1), key='--NAME--')],[sg.Text('User Password:')],[sg.Input(size=(20, 1), key='--PASSWORD--')],[sg.Button('Registration')]],pad=(0,0))]]
    log_in=    [[sg.Frame('Log-In',[[sg.Text('Login Name:')],[sg.Input(size=(20, 1), key='--NAME--')],[sg.Text('Password:')],[sg.Input(size=(20, 1), key='--PASSWORD--')],[sg.Button('Log In')]],pad=(0,0))]]
    layout=[[sg.Column(register),sg.Column(log_in)]]
    window = sg.Window('Reg and Log In', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Registration':
            break
    window.close()


reglog()
