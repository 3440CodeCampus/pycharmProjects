import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import tempfile

mixer.init()
def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang="zh", slow=False )
        tts.save('{}.mp3'.format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

r = sr.Recognizer()

#start = True
#while start == True:
with sr.Microphone() as source:
    print("Say something ! ")
    audio = r.listen(source)

try:
    youSaid = r.recognize_google(audio, language='zh')
    #print("You said: " + r.recognize_google(audio, language='zh-yue'))
    #print("你說: " + youSaid)
    #if youSaid == "bye":

    #    start = False
except sr.UnknownValueError:
    print("Google speech recognition could not understand")
except sr.RequestError as e:
    print("could not request results from google speech recognition service; {0}".format(e))

speak(youSaid)
