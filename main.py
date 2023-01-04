from functions import get_todos, save_todo
from datetime import datetime #or import time ... time.strftime('%b')

date = datetime.today()
# month, day , year= (date.strftime('%b'), date.strftime('%d'), date.strftime('%Y'))
# time = date.strftime('%H:%M:%S')
# print(f'It is {month} {day}, {year} {time}')
today_date_time = date.strftime("%b %d, %Y %H:%M:%S")
print("Add it is time")
print(f'It is {today_date_time}')


# todos = []
while True:
    user_input = input("Type add, show, edit , complete or exit:")
    user_input = user_input.strip()

    # match user_input: #This works just like if and else statement cases
    if user_input.startswith(('add', 'new')): #string or tuple of strings to try #'add' in user_input[0:4]
        # todo = input("Enter a todo:") + '\n' #to send to next line
        todo = user_input[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        save_todo(todos)

    elif user_input.startswith(('show', 'display')): #user_input.startswith('show')
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip()
            print(f'{index+1}-{item}') #because we added 1 here, we have to subtract one from the others
    elif user_input.startswith('edit'): #edit 3
        try: #This works well because we are in a while loop or a loop and the loop wasnt broken
            todos = get_todos()
            old_todo_num = int(user_input[5:]) #edit 3
            old_todo_num = old_todo_num - 1
            todos[old_todo_num] = input('Enter new todo:') + '\n' #reassigning the index
            save_todo(todos)
        except ValueError:
            print("Did not enter a number")
            # user_input = input("Type add, show, edit , complete or exit:")
            # user_input = user_input.strip()
            continue #continue makes the code go back to the top, ignoring the codes below #this can only work in a loop, 
                    #this is the opposite of break statement

    elif user_input.startswith('complete'):
        try:
            todos = get_todos()
            number = int(user_input[9:])
            index = number-1
            todo_to_remove = todos[index]
            todos.pop(index) #since pop works with python indexing, but we are starting from 1,2,3,4
            save_todo(todos)
            message = f"Todo '{todo_to_remove.strip()}' was removed from the list"
            print(message)
        except IndexError as e:
            print(e)
            continue
        
    elif user_input.startswith('exit'):
        break
    else: #This acts as an else statement and the variable doesnt have to be predefined ,you can also use _
        print("Hey, you have entered an unknown command")

print('Bye!')

# a = 'tex.rsfr.bgffd'
# a.replace('.', '_', 1)

    