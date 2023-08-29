FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH): #This is called a custom function
    with open(filepath, 'r') as file_local:
        readtodos = file_local.readlines()
    return readtodos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




