# Озвучка текста с gtts (Google Text-to-Speech)
from gtts import gTTS
import random

# Создайом функцию для озвучки 
def voiceover(text,language,filedr):
    tts = gTTS(text=text, lang=language) # Вызываем функцию gTTS и передейом аргументы текст и язык 
    tts.save(filedr) # Сахраняем аудио файл 

# Создайом функцию main 
def main():
    tex = "Я объязательно победу, и получу Mackbook Air !!!."
    lang = 'ru'
    fldr = 'out.mp3'
    voiceover(tex,lang,fldr)

# Запускаем код 
if __name__=='__main__':
    main()