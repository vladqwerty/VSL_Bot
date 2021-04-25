from os import path

import logging

import speech_recognition as sr
from pyffmpeg import FFmpeg


def voice_to_text(voice_file: str) -> str:
    voice_message_name = voice_file.split(".oga")[0]

    ff = FFmpeg(voice_file)
    ff.convert(voice_file, f"{voice_message_name}.wav")

    audio_file = path.join(f"{voice_message_name}.wav")

    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        res = r.recognize_google(audio, language="ru-RU")
        return res
    except sr.UnknownValueError:
        print("Ничего не понятно =(")
    except sr.RequestError as err:
        logging.exception(err)


if __name__ == "__main__":
    print(voice_to_text("real.ogg"))