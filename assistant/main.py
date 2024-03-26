import config 
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text
import webbrowser
import random


print(f"{config.VE_NAME}", f"{config.VA_ALIAS}", tts.va_speak("Нуми начала свою работу ..."), "Нуми начала свою работу")

# print(f"{config.vh['name']}", f"{config.vh['alias']}", tts.va_speak("Нуми начала свою работу ..."), "Нуми начала свою работу")

print('Список команд:\n \
        list: список команд, команды, что ты умеешь,\n\
        time: время, текущее время, сейчас времени, который чаc,\n\
        joke: расскажи анекдот, рассмеши, шутка, расскажи шутку, пошути, развесели,\n\
        open_browser_youtube: открой мультимедиа,\n\
        open_browser_github: открой код, \n\
        open_browser_server: открой сервер, запусти сервер, \n\
        poem: расскажи стиx, прочитай стиx\n\
        open_steam: открой стим, запусти стим \n\
        open_sharex: снимок, снимок экрана, \n\
        open_OBS: запись, запись экрана \n\
        exit: выход')

def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in config.VA_CMD_LIST:
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


 # def va_respond(voice: str):
 #    print(voice)
 #    if (config.vh['alias']):
 #        # обращаются к ассистенту
 #        cmd = recognize_cmd(filter_cmd(voice))
 #        if cmd['cmd'] not in config.vh['cmd_list']:
 #            tts.va_speak("Что?")
 #        else:
 #            execute_cmd(cmd['cmd'])



def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()
    
    return cmd

# def filter_cmd(raw_voice: str):
#     cmd = raw_voice

#     for x in config.vh['alias']:
#         cmd = cmd.replace(x, "").strip()

#     for x in config.vh['tbr']:
#         cmd = cmd.replace(x, "").strip()
    
#     return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

# def recognize_cmd(cmd: str):
#     rc = {'cmd': '', 'percent': 0}
#     for c, v in config.vh['cmd_list'].items():

#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > rc['percent']:
#                 rc['cmd'] = c
#                 rc['percent'] = vrt

#     return rc


#help
def execute_cmd(cmd: str):
    if cmd == 'list':
        # help
        text = "Я умею: ..."
        text += "рассказывать анекдот+ы ..."
        text += "рассказывать стих+и ..."
        text += "и открыв+ать браузер" 
        # - нет не умеешь
        tts.va_speak(text)
        pass
    
# time
    elif cmd == 'time':
        # current time
        now = datetime.datetime.now()
        text = "В данный момент " + num2text(now.hour) + ":"  + num2text(now.minute)
        tts.va_speak(text)

#poem
    elif cmd == 'poem':
        text = 'ангел грешный, англел мой, забери меня с собой,\n'
        text+= 'уенси меня домой - там сокрой, над широйкою рекой,\n'
        text += 'над широкою водой, ты мне песенку пропой - успокой, что, мол горе, не беда, что надежда есть всегда \n'
        text+= 'что от кривды нет вреда, иногда, \n'
        text+= 'что мол скоро скорро скоро брат мы прибудем в дивный град, где нам всякий будет рад, прямо в Ад\n'
        tts.va_speak(text)
        # tts.va_speak(random.choice(poems))

#joke
    elif cmd == 'joke':
        jokes = ['какая боль, какая боль, повсюду скидки, а денег - ноль', 'виу виу', 'памп памп']
                #  'я могла бы рассказать еще больше, но моему создателю лень']
        tts.va_speak(random.choice(jokes))

#browser
    elif cmd == 'open_browser_youtube':
        text = 'открываю ю+тюб'
        tts.va_speak(text)
        chrome_youtube = "C:/Program Files/Google/Chrome/Application"
        webbrowser.get(chrome_youtube).open("https://youtube.com/watch?v=ABFqbY_rmEk")
        text += 'открыла ю+тюб'
        tts.va_speak(text)
    elif cmd == 'open_browser_github':
        text = 'открываю гет хаб'
        tts.va_speak(text)
        chrome_github = "C:/Program Files/Google/Chrome/Application"
        webbrowser.get(chrome_github).open("https://github.com/PandaBTBs/123/blob/main/config.py")
        text += 'открыла гет хаб'
        tts.va_speak(text)
    elif cmd == 'open_browser_server':
        text = 'открываю сервер веб ю'
        tts.va_speak(text)
        chrome_server = "C:/Program Files/Google/Chrome/Application"
        webbrowser.get(chrome_server).open("https://127.0.0.1:7860")
        text += 'открыла сервер веб ю'
        tts.va_speak(text)

#exit
    elif cmd  == "exit":
        text = "выключаюсь"
        tts.va_speak(text)
        quit()
            
#open programs
    elif cmd == 'open_steam':
        text = 'Открываю стим'
        tts.va_speak(text)
        steamapp = 'pyt(C:/HQ/FF.PY)'
        webbrowser.get(steamapp).open(https://...)
        text+='открыла стим'
        tts.va_speak(text)        
            
    elif cmd == 'open_shar':
        text = 'Открываю снимок экрана'
        tts.va_speak(text)
        sharex = 'pyt(C:/HQ/FF.PY)'
        webbrowser.get(sharex).open(sharex.exe)
        text+='открыла снимок'
        tts.va_speak(text)       

    elif cmd == 'open_OBS':
        text = 'Открываю запись экрана'
        tts.va_speak(text)
        OBS_studio = 'pyt(C:/HQ/FF.PY)'
        webbrowser.get(OBS_studio).open(OBS.exe)
        text+='открыла запись'
        tts.va_speak(text)    
# start lisen programs
stt.va_listen(va_respond)


# import os
# import time
# import speech_recognition as sr
# from fuzzywuzzy import fuzz
# import pyttsx3
# import datetime

# #settings
# opts = {
#     "alias": ('fox'),
#     "tbr": ('say', 'tell', 'show', 'how much', 'say'),
#     "cmds": {
#         "ctime": ('current time', 'now is the time', 'what time is it'),
#         "radio": ('turn on the music', 'play the radio', 'turn on the radio'),
#         "stupid1": ('tell a joke', 'make me laugh', 'you know jokes')
#     }
# }


# #the functions
# def speak(what):
#     print(what)
#     speak_engine.say(what)
#     speak_engine.runAndWait()
#     speak_engine.stop()


# def callback(recognizer, audio):
#     voice = recognizer.recognize_google(audio, language="en-EN").lower()
#     print("[log] Recognized: " + voice)

#     try:

#         if voice.startswith(opts["alias"]):
#             # turn to fox
#             cmd = voice

#             for x in opts['alias']:
#                 cmd = cmd.replace(x, "").strip()

#             for x in opts['tbr']:
#                 cmd = cmd.replace(x, "").strip()

#             # recognize and execute the command
#             cmd = recognize_cmd(cmd)
#             execute_cmd(cmd['cmd'])

#     except sr.UnknownValueError:
#         print("[log] Voice not recognized!")
#     except sr.RequestError as e:
#         print("[log] Unknown error, check internet!")


# def recognize_cmd(cmd):
#     RC = {'cmd': '', 'percent': 0}
#     for c, v in opts['cmds'].items():
#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > RC['percent']:
#                 RC['cmd'] = c
#                 RC['percent'] = vrt

#     return RC


# def execute_cmd(cmd):
#     if cmd == 'ctime':
#         # say current time
#         now = datetime.datetime.now()
#         speak("Now " + str(now.hour) + ":" + str(now.minute))

#     elif cmd == 'radio':
#         # play radio
#         os.system("D:\\Music")

#     elif cmd == 'stupid1':
#         # tell a joke
#         speak("My developer did not teach me jokes ... Ha ha ha")

#     else:
#         print('Command not recognized, retry!')


# #launch
# r = sr.Recognizer()
# m = sr.Microphone(device_index=1)

# with m as source:
# r.adjust_for_ambient_noise(source)

# speak_engine = pyttsx3.init()


# #Only if you have installed voice for speech synthesis!
# voices = speak_engine.getProperty('voices')
# speak_engine.setProperty('voice',voices[1].id)

# #forced cmd test
# speak("My developer did not teach me jokes ...")

# #speak("Good afternoon lord")
# #speak("Fox is listening")

# #stop_listening = r.listen_in_background(m, callback)
# #while True: time.sleep(0.1) # infinity loop
