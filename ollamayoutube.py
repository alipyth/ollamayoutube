# from ollama import Client
#
#
# client = Client(host='http://localhost:11434')
# response = client.chat(model='qwen2.5', messages=[
#   {
#     'role': 'user',
#     'content': 'سلام حال شما چطوره',
#   },
# ])
# print(response['message']['content'])


#_____________________________________________________________________

# import requests
#
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
# }
#
# x = "hello my name is ali , i like ollama library"
# data = f'''{{
#   "model": "llama3.2:1b",
#   "prompt": "translate this into fluent persian {x}",
#   "stream": false
# }}'''
#
# response = requests.post('http://localhost:11434/api/generate', headers=headers, data=data)
# print(response.json()['response'])


#_____________________________________________________________________

# import streamlit as st
# from langchain_community.llms import Ollama
# 
# inp = st.text_input('prompt')
# but  = st.button('lets go')
# if but and inp != "":
#     llm = Ollama(model="qwen2.5")
#     s = llm.invoke(inp)
#     st.markdown(s)



