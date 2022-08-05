from PySimpleGUI import PySimpleGUI as sg
import Client_Socket as cs

sg.theme('DarkBrown')

# Colunas
column_to_be_centered = [
    [sg.Text("Type your message", justification='c')],
    [sg.Multiline(key="mensagem", size=(30,15), justification='c')],
    [sg.Button("Save")]]


# Centraliza as colunas

layout = [[sg.VPush()],
          [sg.Push(), sg.Column(column_to_be_centered, element_justification='c'), sg.Push()],
          [sg.VPush()]]

window = sg.Window("Daily Letter", layout)

cs.start()

while True:
    event, values = window.read()
    # Fecha a janela se o usuario aperta OK
    if event == sg.WIN_CLOSED:
        break
    if event == 'Save':
        msg = (values['mensagem'])
        cs.send_msg_to_server(f'{msg}')
        break

window.close()
