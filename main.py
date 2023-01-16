import streamlit as st

def add_activity():
    item=st.session_state['new_item']
    with open('todos.txt','a') as file:
        file.write(item+'\n')

def update_activity(content):
    with open('todos.txt','w') as file:
        file.writelines(content)

with open ('todos.txt','r') as file:
    content=file.readlines()

st.title('Todo App')
st.subheader('This is my todo app ')
st.write('The app is made to study "streamlib". ')

for index, item in enumerate(content):
    # print(item)
    checkbox=st.checkbox(item.strip('\n'),key=item)
    if checkbox == True:
        print(index,item)

        print(content)
        content.remove(item)
        print(content)
        update_activity(content )

        del st.session_state[item]
        st.experimental_rerun()

# st.session_state
st.text_input(label='Enter a new activity',
              placeholder='Write an activity',
              on_change=add_activity,
              key='new_item')