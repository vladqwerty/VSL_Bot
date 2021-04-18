import speech_recognition as sr
from os import path
from pyffmpeg import FFmpeg

voice_message = "real.ogg"

def voice_to_text(voice_file: str) -> None:
    voice_message_name = voice_message.split('.')[0]
    dirname = path.dirname(path.realpath(__file__))
           
    ff = FFmpeg(path.join(dirname, "audio_test/"))
    ff.convert(path.join(dirname, f"audio_test/{voice_message}"), f"{voice_message_name}.wav")

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), f"audio_test/{voice_message_name}.wav")

    r = sr.Recognizer()
    
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
    try:
        print(r.recognize_google(audio, language="ru-RU"))
    except sr.UnknownValueError:
        print("Ничего не понятно =(")
    except sr.RequestError as e:
        print(f"Что-то пошло не так... {e}")
voice_to_text(voice_message)
