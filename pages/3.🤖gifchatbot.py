import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv
import os
import ssl
os.environ['CURL_CA_BUNDLE'] = ''

session = requests.Session()
session.verify = ssl.CERT_NONE

def load_lottieurl(url: str):
    r = requests.get(url)
    
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")


# load the Environment Variables.
load_dotenv()
st.set_page_config(page_title="OpenAssistant Powered Chat App")

# Sidebar contents
with st.sidebar:
    st.title('📚🤖CAREER BOT')
    st.markdown('''
    ## About
            WELCOME TO THE CAREER BOT
            
    - A INTERACTIVE BOT HELPS TO CHOOSE YOUR CAREER
    - HAVE A FREE CONVERSATION WITH THE CAREER BOT
    - HELPS YOU TO GAIN MORE INFORMATIONS ON NEW CAREERS

    ''')
    add_vertical_space(3)
    st.write('Made with ❤️ by EdXperts')
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        height=None,
        width=None,
        key=None,
    )

st.header("Your Personal CareerBot 💬")



def main():
    global flag
    # Generate empty lists for generated and user.
    # Assistant Response
    
    if 'generated' not in st.session_state:
        st.session_state['generated'] = [
            "HEY!!! , I'm CareerBOT?\n Enter your most intrested hobby!"]
        input_file = open("C://Users//sanch//OneDrive//Desktop//multipage//Questions.txt", "r")
        output_file = open("C://Users//sanch//OneDrive//Desktop//multipage//nn.txt", "w")
        for line in input_file:
          output_file.write(line)

        input_file.close()
        output_file.close()

    # user question
    if 'user' not in st.session_state:
        st.session_state['user'] = ['Hi!']

    # Layout of input/response containers
    response_container = st.container()
    colored_header(label='', description='', color_name='red-30')
    input_container = st.container()

    # get user input
    def get_text():
        input_text = st.text_input("You: ", "", key="input")
        return input_text

    # Applying the user input box
    with input_container:
        user_input = get_text()

    def chain_setup():

        template = """<|prompter|>{question}<|endoftext|>
        <|assistant|>"""

        prompt = PromptTemplate(
            template=template, input_variables=["question"])

        llm = HuggingFaceHub(
            repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens": 1200})

        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt
        )
        return llm_chain

    
    file_path = "C://Users//sanch//OneDrive//Desktop//multipage//nn.txt"
    # generate response
    def generate_response(question, llm_chain):
        response = llm_chain.run(question)
        with open(file_path, 'r') as file:
            one_line = file.readline()
            response = response+"\n"+one_line
            lines = file.readlines()
        if lines:
            first_line = lines[0]
            lines = lines[1:]
            lines.append(first_line)
            with open(file_path, 'w') as file:
                file.writelines(lines)

        return one_line

    # load LLM
    llm_chain = chain_setup()

    # main loop
    with response_container:
        if user_input:
            with open("C://Users//sanch//OneDrive//Desktop//multipage//mm.txt", "a") as file:
                file.writelines(user_input)
                file.close()
            response = generate_response(user_input, llm_chain)
            st.session_state.user.append(user_input)
            st.session_state.generated.append(response)
 
              
            

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['user'][i],
                        is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))
    
    



if __name__ == '__main__':
  main()
  
