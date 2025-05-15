import os
import eel


from engine.features import *
from engine.command import *
eel.init("www")

playAssistantSound()

# open browser at localhost:8000
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# start eel server at localhost:8000
eel.start('index.html', mode=None, host='localhost', port=8000, block=True)
