import PySimpleGUI as sg


def reglog():
    register = [[sg.Frame('Registration',[[sg.Text('User Login Name:')],[sg.Input(size=(20, 1), key='--REG_NAME--')],[sg.Text('User Password:')],[sg.Input(size=(20, 1), key='--REG_PASSWORD--')],[sg.Button('Registration')]],pad=(0,0))]]
    log_in=    [[sg.Frame('Log-In',[[sg.Text('Login Name:')],[sg.Input(size=(20, 1), key='--LOG_NAME--')],[sg.Text('Password:')],[sg.Input(size=(20, 1), key='--LOG_PASSWORD--')],[sg.Button('Log In')]],pad=(0,0))]]
    output= [[sg.Frame('Output',[[sg.Output(size=(50,20),key='--OUTPUT--')]])]]
    layout=[[sg.Column(register),sg.Column(log_in)],output]
    window = sg.Window('Reg and Log In', layout,location=(300,100))
    while True:
        event, values = window.read()
        if event == 'Registration':
            reg_name=values['--REG_NAME--']
            reg_password=values['--REG_PASSWORD--']
            from source_files.register import reg
            window['--OUTPUT--'].update(reg(reg_name,reg_password))
        if event=='Log In':
            log_name=values['--LOG_NAME--']
            log_password=values['--LOG_PASSWORD--']
            from source_files.log_in import log
            window['--OUTPUT--'].update(log(log_name,log_password))
        if event== sg.WINDOW_CLOSED:
            break
    window.close()


reglog()
