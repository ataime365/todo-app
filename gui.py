from functions import get_todos, save_todo
import PySimpleGUI as sg #sg == simple gui

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To_Do App", layout=[[label], [input_box, add_button]])
# window.read() #This displays the window on the screen #The biggest and most useful method

# Event Loop to process "events" and get the "values" of the inputs
# while True:
values = window.read()

# if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    # break
print('You entered ', values)

window.close()