import pyttsx3
import speech_recognition as sr


def get():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("di algo..")
        audio =r.listen(source)
        print("listo!")

    try:
        text= r.recognize_google(audio)
        print('dijiste'+text)

    except Exception as e:
        print(e)

get()




