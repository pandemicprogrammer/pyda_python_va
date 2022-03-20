# Virtual Assistant, Wolfram, SimpleGUI,
# Marie Valentonis

import PySimpleGUI as sg
import wolframalpha 
import keys

API_KEY = 'AYJ4WG-4TH52X9ULY'
client = wolframalpha.Client(API_KEY)



sg.theme('DarkBlue')
# Window content
layout = [  [sg.Text('Welcome to Pyda Virtual Assistant')],
            [sg.Text('What would you like to know?'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Initialize window
window = sg.Window('PyDa', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    res = client.query(values[0])
    sg.Popup(next(res.results).text)

window.close()