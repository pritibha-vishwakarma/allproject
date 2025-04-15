import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()
machine.setProperty('rate', 150)  # Set speaking rate

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "pratibha" in instruction:
                instruction = instruction.replace('pratibha', '')
                print(instruction)
            return instruction
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
    except sr.RequestError:
        talk("Sorry, my speech service is down.")
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred.")
    return ""

def play_pratibha():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', '')
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)
    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
    elif 'what is your name' in instruction:
        talk('I am Pratibha, your personal assistant.')
    elif 'who is' in instruction:
        person = instruction.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Please repeat your command.')

play_pratibha()
