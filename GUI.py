import PySimpleGUI as sg


def reglog():
    register = [[sg.Frame('Registration',[[sg.Text('User Login Name:')],[sg.Input(size=(20, 1), key='--REG_NAME--')],[sg.Text('User Password:')],[sg.Input(size=(20, 1), key='--REG_PASSWORD--')],[sg.Button('Registration')]],pad=(0,0))]]
    log_in=    [[sg.Frame('Log-In',[[sg.Text('Login Name:')],[sg.Input(size=(20, 1), key='--LOG_NAME--')],[sg.Text('Password:')],[sg.Input(size=(20, 1), key='--LOG_PASSWORD--')],[sg.Button('Log In')]],pad=(0,0))]]
    user=[[sg.Frame('User Status',[[sg.Text(size=(40,1),key='--USER_NAME--')]])]]
    output= [[sg.Frame('Output',[[sg.Output(size=(50,20),key='--OUTPUT--')]])]]
    layout=[[sg.Column(register),sg.Column(log_in)],user,output]
    window = sg.Window('Reg and Log In', layout,location=(300,100))
    while True:
        from source_files.auto_check_log import auto
        auto()
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
            back_data=log(log_name,log_password)
            window['--OUTPUT--'].update(back_data)
            window['--USER_NAME--'].update(back_data)
        if event== sg.WINDOW_CLOSED:
            break
    window.close()



reglog()