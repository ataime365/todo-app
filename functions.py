

def get_todos(filepath='todos.txt'): #default argument kwargs
    with open(filepath, 'r') as oldfile:
        todos = oldfile.readlines() #old_todo_list , todos is a list
        return todos

def save_todo(new_todos_list, filepath='todos.txt'):
    with open(filepath, 'w') as f: #This will alway create new file, no matter the mode we choose to use, best things is to read the previous list from the txt file and then add to it.
        f.writelines(new_todos_list)