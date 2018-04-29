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

speak("潮州怒漢")
