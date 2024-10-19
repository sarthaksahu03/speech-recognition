import speech_recognition as sr
import pyttsx3
import re
import tkinter as tk
from tkinter import scrolledtext

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def format_professional(text):
    text = text.capitalize()
    if not text.endswith('.'):
        text += '.'
    text = re.sub(r'\b(um|uh|like)\b', '', text)
    return text

def recognize_speech():
    global recognizer  
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            professional_text = format_professional(text)
            text_box.insert(tk.END, professional_text + "\n")
            text_box.see(tk.END)
    except sr.UnknownValueError:
        text_box.insert(tk.END, "Could not understand audio\n")

window = tk.Tk()
window.title("Speech to Text Converter")

text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
text_box.pack(padx=10, pady=10)

recognize_button = tk.Button(window, text="Start Listening", command=recognize_speech, font=("Arial", 12))
recognize_button.pack(padx=10, pady=10)

window.mainloop()
