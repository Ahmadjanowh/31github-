# Извдечаем аудио их видео с помоши библиотеки moviepy
# Может в дальнейшом сделаем телеграм бот 
# pip install moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip('audio_from_video/consta.mp4') # Указываем путь к видео 
audio = video.audio 
audio.write_audiofile('audio_from_video/my_audio.mp3') # Получает аудио 
# Таким оброзом за 5 строк без комнетов мы можем выташить аудио из видео 