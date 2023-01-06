from functions import get_todos, save_todo
import PySimpleGUI as sg #sg == simple gui

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
close_btn = sg.Button("Close") 

window = sg.Window("My To_Do App", layout=[[label], [input_box, add_button], [close_btn]],
                        font=('Helvetica', 20))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() #This displays the window on the screen #The biggest and most useful method
    print(event, values)
    if event == 'Add':
        todos_li = get_todos()
        new_todo = values['todo'] + '\n'
        todos_li.append(new_todo)
        save_todo(todos_li)
    elif event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break #This break statement enable window.close() to be accesible


window.close() # Window is closed only after the while loop ends