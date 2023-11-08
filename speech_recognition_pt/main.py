# Распознование речи 
# pip install SpeechRecognition
# pip install pyaudio - для работы с микрофоном 

import speech_recognition as sr

# Создайте объект Recognizer
recognizer = sr.Recognizer()

# Захватите аудио с микрофона
with sr.Microphone() as source:
    print("Я вас слушаю...")
    
    audio = recognizer.listen(source)

# Попробуйте распознать речь с помощью Google Web Speech API
try:
    text = recognizer.recognize_google(audio,language='ru-RU') 
    print("Вы сказали: " + text)

except sr.UnknownValueError:
    print("Извините, не удалось распознать речь")
except sr.RequestError as e:
    print("Произошла ошибка при отправке запроса к сервису Google: {0}".format(e))