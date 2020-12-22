# coding: utf-8
# author: xuyang
# created_time: 2020/12/19

from comtypes.client import CreateObject
from comtypes.gen import SpeechLib

engine = CreateObject('SAPI.SpVoice')
stream = CreateObject('SAPI.SpFileStream')

infile = 'demo.txt'
outfile = 'demo_audio.wav'

stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream

f = open(infile, 'r', encoding='utf-8')
theText = f.read()
f.close()

engine.speak(theText)
stream.close()

