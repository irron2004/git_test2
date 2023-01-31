import streamlit as st
import pandas as pd
import os

def refresher():
    mainDir = os.path.dirname(__file__)
    filePath = os.path.join(mainDir, 'main.py')
    with open(filePath, 'r') as f:
        code = f.read()
    
    with open(filePath, 'w') as f:
        code += '#'
        f.write(code)
        

op_list = ['OP1','OP2','OP3']
server_list = ['server1','server2','server3']


def load_data():
    if 'op_result.csv' in os.listdir():
        op_result = pd.read_csv('op_result.csv')
    else:    
        op_result = pd.DataFrame({'OP1' : ['사용가능'],
                    'OP2': ['사용가능'],
                    'OP3': ['사용가능'],
                    'server1' : ['사용가능'],
                    'server2' : ['사용가능'],
                    'server3' : ['사용가능']
                })
    return op_result

op_result = load_data()
st.dataframe(op_result)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)


with col1:
    op_result = load_data()
    st.write('사용할 서버를 입력해주세요')
    user_name = st.text_input(
        "사용자 이름",
        key="placeholder",
    )
    # if user_name:
    op_name = st.selectbox('사용할 OP', op_list)
    server_name = st.selectbox('사용할 server', server_list)
    op_result[op_name] = user_name
    op_result[server_name] = user_name
    if st.button('save'):
        op_result.to_csv('./op_result.csv',index = False)
        refresher()

with col2:
    op_result = load_data()
    st.write('사용 완료한 사용자를 입력해주세요')
    complete_op_name = st.selectbox('사용할 OP', op_list,key='2')
    complete_server_name = st.selectbox('사용할 server', server_list,key='3')

    op_result[complete_op_name] = '사용가능'
    op_result[complete_server_name] = '사용가능'
    if st.button('save',key ='1'):
        op_result.to_csv('op_result.csv',index = False)
        refresher()###########