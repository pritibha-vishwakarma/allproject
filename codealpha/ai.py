import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
   machine.say(text)
   machine.runAndWait()

def input_instruction():
    global instruction
    instruction=""
    try:
        with aa.Microphone() as origin:
            listener.adjust_for_ambient_noise(origin)
            print("listening")
        speech = listener.listen(origin)
        instruction = listener.recognize_google(speech)
        instruction = instruction.lower()
        if "pratibha" in instruction:
            instruction=instruction.replace(' pratibha', )
            print(instruction)

    except Exception as e:
        print(f"Error:{e}")
        pass
    return instruction

def play_pratibha():

    instruction=input_instruction()
    print(instruction)
    if"play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I: %M%p')
        talk('current time'+time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        talk("Today's date " + date)  
    elif 'how are you' in instruction:
        talk('I am fine, how about you')
    elif 'what is your name' in instruction:
        talk('I am pratibha, what can i do for you')     

    elif 'who is' in instruction:
        human=instruction.replace('what is'," ")  
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)  
    else:
        talk('please repeat')

play_pratibha()



