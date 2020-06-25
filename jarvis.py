import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random

#for import voice of computer
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#function for speak a string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#funtion for stating(wish)
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir')
    elif hour>=12 and hour<=16:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('I am jarvis, how I can Help You?')

#function for take command
def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        r.energy_threshold = 300
        audio=r.listen(source)

    try:
        print('Recognzing....')
        quary=r.recognize_google(audio,language= 'en-in')

        print(f" {quary}\n")
    except Exception as e:
         print('Say that again please..')
         speak('i can not understand, please try again')
         return'None'
    return quary


#path of chrome for open in chrome
browser=webbrowser.get('C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s')


if __name__=="__main__":
    wishme()
    while True:
        quary= takecmd().lower()


#if not recognize
        if 'none' in quary:
            pass

#for wikipedia
        elif 'wikipedia' in quary:
            quary=quary.replace('wikipedia','')
            result=wikipedia.summary(quary, sentences=2)
            speak('according to wikipedia')
            print(result)
            speak(result)

#for opening youtube
        elif 'open youtube' in quary:
             speak("opening youtube")
             browser.open('youtube.com')

#for opening google.com
        elif 'open google' in quary:
            speak('opening google')
            browser.open('google.com')

#for opening gmail
        elif 'open gmail' in quary:
            speak('opening gmail')
            browser.open('gmail.com')

#for usual talk
        elif 'how are you' in quary:
            speak('i am fine, thank you')
            speak("what's about you?")
        elif 'i am fine' in quary:
            speak('okk')
            speak('how i can help you?')
        elif 'what you can do' in quary:
            speak('i can open youtube,i can search on wikipedia and if you are ofline then i can play song for you')
            speak('what you want')

#for exit from proggram
        elif 'exit' in quary:
            speak('bye. see you again')
            break

#for playing new gujarati song
        elif'play new gujarati' in quary:
            ran_guj_song = random.choice(range(1, 9))
            new_guj_music_dir='E:\\new gujrati song'
            song=os.listdir(new_guj_music_dir)
            speak('playing new gujarati song')
            print(song[ran_guj_song])
            os.startfile(os.path.join(new_guj_music_dir,song[ran_guj_song]))

#for playing new hindi song
        elif 'play new hindi' in quary:
            ran_hin_song= random.choice(range(1, 48))
            new_hin_music_dir = 'E:\\new song'
            song = os.listdir(new_hin_music_dir)
            speak('playing new hindi song')
            print(song[ran_hin_song])
            os.startfile(os.path.join(new_hin_music_dir, song[ran_hin_song]))


#for opening vice city folder
        elif 'play game' in quary:
            speak("let's play vice city")
            game_dir='E:\\dev\\gta vice city.com'
            os.startfile(os.path.join(game_dir))

 #for opening python
        elif "coding" in quary:
            speak("let's do coding with python")
            py_dir='C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.8\\IDLE (Python 3.8 32-bit)'
            os.startfile(os.path.join(py_dir))

 #for opening mozilla firefox
        elif "open firefox" in quary:
            speak("openig, mozilla firefox")
            firefox_dir='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox'
            os.startfile(os.path.join(firefox_dir))


#for opening microsoft word
        elif 'open microsoft word' in quary:
            speak('opening, microsoft word')
            word_dir='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007'
            os.startfile(os.path.join(word_dir))


 #if no condition apply from above then it automatically search on google
        elif '' in quary:
            x= quary.replace('', '')
            q='https://www.google.com/search?q='+x
           # print(q)
            browser.open(q)
