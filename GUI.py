import PySimpleGUI as sg


def reglog():
    register = [[sg.Frame('Registration',[[sg.Text('User Login Name:')],[sg.Input(size=(20, 1), key='--NAME--')],[sg.Text('User Password:')],[sg.Input(size=(20, 1), key='--PASSWORD--')],[sg.Button('Registration')]],pad=(0,0))]]
    log_in=    [[sg.Frame('Log-In',[[sg.Text('Login Name:')],[sg.Input(size=(20, 1), key='--NAME--')],[sg.Text('Password:')],[sg.Input(size=(20, 1), key='--PASSWORD--')],[sg.Button('Log In')]],pad=(0,0))]]
    output= [[sg.Frame('Output',[[sg.Output(size=(50,20),key='--OUTPUT--')]])]]
    layout=[[sg.Column(register),sg.Column(log_in)],output]
    window = sg.Window('Reg and Log In', layout,location=(300,100))
    while True:
        event, values = window.read()
        if event == 'Registration':
            name=values['--NAME--']
            password=values['--PASSWORD--']
            from source_files.register import reg
            reg(name,password)
            window['--OUTPUT--'].update("Már van ilyen felhasználó")
        if event== sg.WINDOW_CLOSED:
            break
    window.close()


reglog()
