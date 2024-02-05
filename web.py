import streamlit as st
import functions


todos = functions.get_todos()
print(st.session_state)

if 'added_todo' not in st.session_state:
    st.session_state.added_todo = ''


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state.added_todo = st.session_state.new_todo
    st.session_state.new_todo = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo + str(index))
    if checkbox:
        print(todo + str(index))
        todos.pop(index)
        functions.write_todos(todos)
        print(st.session_state)
        del st.session_state[todo + str(index)]
        st.rerun()

st.text_input(label="Enter a todo", label_visibility="hidden", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")

st.write(f'Last submission: {st.session_state.added_todo}')

# st.session_state
