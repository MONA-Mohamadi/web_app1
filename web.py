import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    todo_arg = st.session_state['new_todo'] + '\n'
    todos.append(todo_arg)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write('This App helps you increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label=' ', placeholder='Add a to do ...',
              on_change=add_todo, key='new_todo')
