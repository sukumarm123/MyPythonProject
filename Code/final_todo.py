#from function_final_todo import read_todos, write_todos
import function_final_todo
import time


now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is", now)
while True:
    user_action=input("enter add, show, edit, complete or exit: ")
    user_action=user_action.strip() #.strip use to delet the space and take only the string value

    if user_action.startswith("add"):
        todo = user_action[4:] #This [4:] means list will save from index no 4 before that it will not accept

        todos = function_final_todo.read_todos()

        todos.append(todo + '\n') #use append to add the items in the list

        function_final_todo.write_todos(todos)

        print("Todo is added.")

    elif user_action.startswith("show"):

        todos = function_final_todo.read_todos()

        for index, item in enumerate(todos): #use for loop tom print the value only without bracke and colon
            item = item.title() #use title to make the first leter upper case
            # print((index+1),'-',item) #if we use print it will print a space between them.
            item = item.strip('\n')
            result = f"{index + 1}-{item}" #f string remove the unnecessary space betwwn the strings
            print(result)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number-1

            todos = function_final_todo.read_todos()

            new_todo = input("Enter New Todo: ")
            todos[index] = new_todo + '\n'

            function_final_todo.write_todos(todos)
            print("Edit Successful")

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = function_final_todo.read_todos()

            index = (number - 1)
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index) #use pop function to clear list using index

            function_final_todo.write_todos(todos)

            message = f"Todo - '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number. Please try another number.")
            continue

    elif user_action.startswith("exit"):
        break

    else: #for unknowen command
        print("Unknown Command")

print("Thank You")
