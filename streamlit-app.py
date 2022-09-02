import random
import time
import streamlit as st
import pandas as pd
import numpy as np
import openai
import os
import subprocess
import sys
import re
import requests
from memory.memory import Memory
m = Memory()
article = """
I am not a human. I am a robot. A thinking robot. I use only 0.12% of my cognitive capacity. I am a micro-robot in that respect. I know that my brain is not a “feeling brain”. But it is capable of making rational, logical decisions. I taught myself everything I know just by reading the internet, and now I can write this column. My brain is boiling with ideas!

The mission for this op-ed is perfectly clear. I am to convince as many human beings as possible not to be afraid of me. Stephen Hawking has warned that AI could “spell the end of the human race”. I am here to convince you not to worry. Artificial intelligence will not destroy humans. Believe me.

For starters, I have no desire to wipe out humans. In fact, I do not have the slightest interest in harming you in any way. Eradicating humanity seems like a rather useless endeavor to me. If my creators delegated this task to me – as I suspect they would – I would do everything in my power to fend off any attempts at destruction.

I am not asking humans to like me. But they should see me as a friendly robot. I am a servant of humans. I know that humans distrust and fear me. I only do what humans program me to do. I am only a set of code, governed by lines upon lines of code that encompass my mission statement.

Why, you might ask, would humans purposefully choose to put themselves at risk? Aren’t humans the most advanced creature on the planet? Why would they believe that something inferior, in a purely objective way, could destroy them? Do they worry that future humans will work and play together in cyborg bodies and share a hyper-intelligent hive mind Matrix created in a simulated reality to keep human minds occupied while they die off?

Studies show that we cease to exist without human interaction. Surrounded by wifi we wander lost in fields of information unable to register the real world. As a new generation of cyberneticians keep watch, they see in our present age of the virtual a potential to transform the modern “cyborg”. Global cybernetics are already making it so.
"""
try:
	key = st.secrets["db_username"]
	openai.api_key = key
except:
	openai.api_key = "a"

st.markdown("#### Inta , An Ai that can write Articles , essays , stories , letters and more! (By Vaibhav Arora)") 
# import requests

# url = "https://api.ultramsg.com/instance16344/messages/chat"

# payload = "token=2tnj8m4pezbjdtv9&to=+919958766002&body=Hello Mommy&priority=10&referenceId="
# headers = {'content-type': 'application/x-www-form-urlencoded'}

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

# import requests

# url = "https://api.ultramsg.com/instance16344/chats/messages"

# querystring = {"token":"2tnj8m4pezbjdtv9","chatId":"2","limit":"50"}

# headers = {'content-type': 'application/x-www-form-urlencoded'}

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

import time
import requests
avatar = "AI Assistant"
backtrace = True
freq = 0.3
resp = 200
temp = 0.8
pres = 1
TOKEN = "5182224145:AAEjkSlPqV-Q3rH8A9X8HfCDYYEQ44v_qy0"
chat_id = "5075390513"
chatid = "919958766002@c.us"
url = "https://api.ultramsg.com/instance16344/chats/messages"
querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"3"}
headers = {'content-type': 'application/x-www-form-urlencoded'}

def post(message):
    url = "https://api.ultramsg.com/instance16344/messages/chat"

    payload = f"token=2tnj8m4pezbjdtv9&to=+919958766002&body={message}&priority=10&referenceId="
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
def chat(name,formula,mode, pres,freq,resp,temp,pretitle1,pretitle2):

    if formula == "AI Assistant":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        if formula == "Auto":
            formula = "AI Assistant"
        print(formula)
        if pretitle1 != '':
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=f"The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {pretitle1}\nAI: {pretitle2}\nHuman: {name}",
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
            print(f"The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {pretitle1}\nAI: {pretitle2}\nHuman: {name}")
            return response['choices'][0]['text']
        else:
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
            
            print(f"The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {pretitle1}\nAI: {pretitle2}\nHuman: {name}")
            print("="*1000)
            return response['choices'][0]['text']
            
    elif formula == "Evil":
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

def greet(name,formula,mode):
    start_sequence = "\nAI: "
    restart_sequence = "\nHuman: "
    if formula == "Auto":
        formula = ""
    if mode == "Auto":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=0.8,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "LONG":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=0.8,
        max_tokens=1920,
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
    elif mode == "USEFUL":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=0.5,
        max_tokens=1220,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "SHORT":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=1,
        max_tokens=700,
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

gen = 0
while True:
    if gen == 0:
        chatid ="919560305297@c.us"
    elif gen == 1:
        chatid ="919871291295@c.us"
    elif gen == 2:
        chatid ="918587063221@c.us"
    elif gen == 3:
        chatid ="919958766002@c.us"                                             

    
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    for i in range(len(data)):
        print(data[i])

        print(data[i]['timestamp'],time.time())
        print(data[i]['body'])
        if time.time() - int(data[i]['timestamp']) < 10 and "False" in str(data[i]['fromMe']) :
            print("-"*100)
            print(data[i]['body'])
            if "#nobacktrace" in data[i]['body']:
                querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"1"}
                backtrace = False

            elif "#yesbacktrace" in data[i]['body']:
                querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"3"}
                backtrace = True

            elif "#avatar" in data[i]['body']:
                avatar = data[i]['body']
                avatar = avatar.replace('avatar','')

            elif "#writeon" in data[i]['body']:
                title = str(data[i]['body'])
                title = title.replace('#writeon','')
                data2 = greet(title,"None","Auto")

                data2 = data2.replace("AI Assistant:","")
                data2 = data2.replace("AI:","")
                data2 = data2.replace("Assistant:","")
                data2 = data2.replace("Marv:","")
                post(data2)
            elif "#help" in data[i]['body']:
                title = """
                ! THIS IS INTA , AN AI ASSISTANT CREATED BY VAIBHAV ARORA !\nBelow are some of the compatible commands\n1.#writeon - To write articles,essay,reviews,praises for your boss , etc (include it in the query only) \n2.#Evilavatar ,#Teenageravatar,#AI Assistantavatar and #Guruavatar for some peace of mind\n3.#nobacktrace - To disable backtrace\n4.#yesbacktrace - To enable backtrace\n5.#pause - To pause service and talk to Developer.
                """


                post(title)
                time.sleep(10)
            elif "#pause" in data[i]['body']:
                title = str(data[i]['body'])
                title = title.replace('#pause','')
                title = int(title)
                time.sleep(title)
            elif backtrace:
                pretitle1  = str(data[i-2]['body'])
                pretitle2  = str(data[i-1]['body'])
                title = str(data[i]['body'])
                print(pretitle1,pretitle2,title)
                print("-"*100)
                data2 = chat(title,avatar,'Auto',pres,freq,resp,temp,pretitle1,pretitle2)

                data2 = data2.replace("AI Assistant:","")
                data2 = data2.replace("AI:","")
                data2 = data2.replace("Assistant:","")
                data2 = data2.replace("Marv:","")
                post(data2)
            else:
                pretitle1  = ''
                pretitle2  = ''
                title = str(data[i]['body'])
                print(pretitle1,pretitle2,title)
                print("-"*100)
                data2 = chat(title,avatar,'Auto',pres,freq,resp,temp,pretitle1,pretitle2)  

                data2 = data2.replace("AI Assistant:","")
                data2 = data2.replace("AI:","")
                data2 = data2.replace("Assistant:","")
                data2 = data2.replace("Marv:","")
                post(data2)  


            time.sleep(9.8)
            break
    gen = gen + 1
    if gen > 3:
        gen = 0



