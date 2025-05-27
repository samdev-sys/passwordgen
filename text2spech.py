import pyttsx3

engine=pyttsx3.init()
saludo=input("ingresa tu frase o saludo")
engine.say(saludo)

engine.runAndWait()