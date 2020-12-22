# coding: utf-8
# author: sirxy
# created_time: 2020/12/19

import speech_recognition as sr

audio_file = 'demo_audio.wav'

r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
	audio = r.record(source)

try:
	print('文本内容：', r.recognize_sphinx(audio, language='zh-CN'))
	print('文本内容', r.recognize_sphinx(audio))
except Exception as e:
	print(e)

'''
missing PocketSphinx language data directory: "D:\Python 3.7.3\lib\site-packages\speech_recognition\pocketsphinx-data\zh_CN"
'''
# https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst
