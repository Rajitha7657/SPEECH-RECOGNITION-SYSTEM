# app.py

import streamlit as st
import speech_recognition as sr
import pyttsx3
import tempfile

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

st.title("🎤 Speech to Text & Text to Speech App")

st.write("This app listens to your voice, transcribes it to text, and can read it back to you!")

# Button to start recording
if st.button("🎙️ Start Recording"):
    st.info("Recording... Please speak now!")
    
    # Using microphone
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)
            
            st.success("Recording complete! Processing...")
            
            # Using Google Web Speech API
            recognized_text = recognizer.recognize_google(audio)
            recognized_text = recognized_text.lower()
            
            st.subheader("📝 Recognized Text:")
            st.write(recognized_text)

            if st.button("🔊 Speak Out Loud"):
                speak_text(recognized_text)

        except sr.RequestError:
            st.error("Could not request results from Google Speech Recognition service.")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")


