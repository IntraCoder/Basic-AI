import os
import time
import pyautogui
import pyttsx3 as pt
from listen import *


# you need to install pyaudio and pyttsx3 modules


def speak(text):
    pt.speak(text)


speak('''Welcome ! I am Jarvis!
I can assist you with many tasks! just type them down ..''')


def search(web):
    pyautogui.press('browsersearch')
    pyautogui.write(web)
    pyautogui.press('enter')


ctime = time.localtime()
greet = {'hi' or 'hello': 'Hello!', 'how are you?': 'i am fine', 'time': f'{ctime.tm_hour} : {ctime.tm_min} ',
         "today's tasks": ['jog', '9:30 A.M.-meeting',
                           '12 Noon-Lunch with client'], 'bye': 'Thankyou,shall meet again!'}
while True:
    a = listen.listen()
    try:
        for j in a.split():
            if j in greet.keys():
                speak(greet[j])
            elif 'shutdown' in a:
                speak('Are you sure to shutdown?')
                c = listen.listen()
                print(c)
                time.sleep(4)
                speak('shutting down..')
                os.system('shutdown /s /t 1')
            elif 'restart' in a:
                speak('restarting system')
                os.system('shutdown /r /t 1')
            elif 'close' in a:
                speak('Tell name of program')
                program = listen.listen()
                speak(f'closing {program}')
                try:
                    os.system(f'TASKKILL /F /IM {program}.exe')
                except:
                    speak(f'{program} is already closed!')
            elif 'open' in a:
                speak('Tell name of program')
                program = listen.listen()
                try:
                    speak(f'starting {program}')
                    os.startfile(f'{program}')
                except:
                    speak(f'{program} is already running')
            elif 'quit' in a:
                if 18 < ctime.tm_hour < 20:
                    greet = 'evening'
                elif ctime.tm_hour < 12:
                    greet = 'day'
                elif 20 < ctime.tm_hour < 3:
                    greet = 'night'
                speak(f'''ok sir! going to sleep!
                 Have a good   sir...''')
                quit()
                break

            elif 'Search ' in a:
                a.remove('search')
                search(a)
                speak(f'searching {a}')
        if a == 'quit':
            break
    except:
        speak('Please try again')
