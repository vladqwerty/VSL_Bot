from os import path

import logging

import speech_recognition as sr
from pyffmpeg import FFmpeg


def voice_to_text(voice_file: str) -> str:
    voice_message_name = voice_file.split('.')[0]
    dir_name = path.dirname(path.realpath(__file__))

    ff = FFmpeg(path.join(dir_name, "../audio_test/"))
    ff.convert(path.join(dir_name, f"../audio_test/{voice_file}"), f"{voice_message_name}.wav")

    audio_file = path.join(path.dirname(path.realpath(__file__)), f"../audio_test/{voice_message_name}.wav")

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
