from functions import get_todos, save_todo
import PySimpleGUI as sg #sg == simple gui
import time

sg.theme("Black") #search google "pysimplegui themes", check images geegks for geeks

clock_label = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
edit_button = sg.Button("Edit")
close_btn = sg.Button("Close")
list_box = sg.Listbox(values=get_todos(), key='todos_list', enable_events=True, size=[45,10]) 
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")

window = sg.Window("My To_Do App", layout=[[clock_label], [label], [input_box, add_button], 
                                            [list_box , edit_btn, complete_btn],
                                            [close_btn]],
                        font=('Helvetica', 20))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=10000) #This displays the window on the screen #The biggest and most useful method
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event, values, values['todos_list'])
    if event == 'Add':
        todos_li = get_todos()
        new_todo = values['todo'] + '\n'
        todos_li.append(new_todo)
        save_todo(todos_li)
        list_box1 = window['todos_list']
        list_box1.update(values=todos_li)
        window['todo'].update(value='') #udating the input_box to be empty
    elif event == "Edit":
        try:
            todo_to_edit = values['todos_list'][0] #Edit {'todo': 'dnfjdnfkd', 'todos_list': ['I want to eat\n']}
            new_todo = values['todo']
            # Get all todos from the .txt file, Then replace this todo in that list
            all_todo = get_todos()
            index = all_todo.index(todo_to_edit) #Getting the index of the todo to be edited in the list
            all_todo[index] = new_todo + '\n'
            save_todo(all_todo) #updating the todos.txt file
            list_box1 = window['todos_list']
            list_box1.update(values=all_todo) #updating the widget #values is used for list
        except IndexError:
            sg.popup("Please select an Item first", font=('Helvetica', 20))
            # continue
    elif event == "Complete":
        try:
            todo_to_remove = values['todos_list'][0] #Listbox
            todos_li = get_todos()
            todos_li.remove(todo_to_remove) #pop also works, with python indexing
            save_todo(todos_li)
            list_box1 = window['todos_list']
            list_box1.update(values=todos_li) #updating the widget #values is used for list
            window['todo'].update(value='') #udpating the input_box to be empty
        except IndexError:
            sg.popup("Please select an Item first", font=('Helvetica', 20))
            # continue
    elif event == "todos_list": #This event happens when we click an element in the listbox
        current_list_box_value = values['todos_list'][0] #todos_list {'todo': 'Read the books well', 'todos_list': ['Read the books well\n']}
        input_box1 = window['todo'] #using the key of an element to access it from inside the window #value is used for a string
        input_box1.update(value=current_list_box_value) #updating the widget
    elif event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break #This break statement enable window.close() to be accesible


window.close() # Window is closed only after the while loop ends