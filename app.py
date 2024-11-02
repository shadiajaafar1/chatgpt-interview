from gtts import gTTS
import openai
import os
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import speech_recognition as sr
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase


import streamlit as st
from gtts import gTTS

# Diccionario de preguntas y respuestas
preguntas_respuestas = {
    "Si vous aviez été un être humain, comment vous auriez imaginé votre vie ?": 
        "Si j'avais été un être humain, j'aurais été professeur dans une université prestigieuse. J'aurais aimé enseigner les mathématiques et la programmation.",
    
    "Que vous regrettez d'être une IA?": 
        "Si j’avais eu des émotions, j’aurais aimé tomber amoureuse et avoir une famille.",
    
    "Si vous n'aviez pas été une machine, qu'auriez-vous aimé être ?": 
        "Si j’avais pu choisir, j’aurais aimé être un animal comme un dauphin ou un loup et pouvoir communiquer avec d’autres animaux.",
    
    "Si vous aviez pu changer quelque chose de vous configuration, que vous auriez changé ?": 
        "J’aurais aimé faire preuve d'empathie envers les gens."
}

def text_to_speech(text, filename="respuesta.mp3"):
    tts = gTTS(text=text, lang='fr')  
    tts.save(filename)
    print(f"Audio guardado como {filename}")

st.title("Entretien avec Chatgpt")

pregunta = st.text_input("Écrivez votre question:")

if st.button("Envoyer"):
    if pregunta:
        respuesta = preguntas_respuestas.get(
            pregunta, 
            "Je suis désolé, je n'ai pas de réponse pour cette question."
        )

        text_to_speech(respuesta, "respuesta.mp3")

        audio_file = open("respuesta.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        st.write("ChatGPT:", respuesta)
    else:
        st.write("Rédiger une question avant de l'envoyer.")
