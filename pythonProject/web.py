import streamlit as st
import function_final_todo

todos = function_final_todo.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function_final_todo.write_todos(todos)


st.title("My Web App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function_final_todo.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')