import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something ! ")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio, language='zh-yue'))
except sr.UnknownValueError:
    print("Google speech recognition could not understand")
except sr.RequestError as e:
    print("could not request results from google speech recognition service; {0}".format(e))
