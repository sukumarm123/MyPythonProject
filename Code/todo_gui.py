import function_final_todo
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkBlue3")

clock = sg.Text('', key='clock')
label = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key="todo")
add_button = sg.Button(size=2, image_source="add.png", button_color="Green",
                       mouseover_colors="Yellow", tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=function_final_todo.read_todos(),
                      key='todos',
                      enable_events=True,
                      size=[40, 10])
edit_button = sg.Button(size=2, image_source="edit.png", button_color="Green",
                       mouseover_colors="Yellow", tooltip="Edit todo", key="Edit")

complete_button = sg.Button(size=2, image_source="complete.png", button_color="Blue",
                       mouseover_colors="Green", tooltip="Complete todo", key="Complete")

exit_button = sg.Button(size=2, image_source="exit.png", button_color="Blue",
                       mouseover_colors="Red", tooltip="Exit todo", key="Exit")

window = sg.Window('My To Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 17))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(event)
    #print(values)
    match event:
        case "Add":
            todos = function_final_todo.read_todos()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            function_final_todo.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = function_final_todo.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function_final_todo.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica, 15"))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function_final_todo.read_todos()
                todos.remove(todo_to_complete)
                function_final_todo.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica, 15"))

            except ValueError:
                sg.popup("Please select an item first.", font=("Helvetica, 15"))

        case "Exit":
            sg.popup("Thank you.")
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()

