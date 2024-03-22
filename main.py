import pydirectinput
import pyautogui
import speech_recognition as sr
import time


time.sleep(2)#so u can switch to your game
recognizer = sr.Recognizer()




def go_forward():
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('w')

def go_backward():
    pydirectinput.keyDown('s')
    time.sleep(2)
    pydirectinput.keyUp('s')

def go_left():
    pydirectinput.keyDown('a')
    time.sleep(2)
    pydirectinput.keyUp('a')

def go_right():
    pydirectinput.keyDown('d')
    time.sleep(2)
    pydirectinput.keyUp('d')

def slot_1():
    pydirectinput.keyDown('1')
    time.sleep(0.1)
    pydirectinput.keyUp('1')

def jump():
    pydirectinput.keyDown('space')
    time.sleep(0.1)
    pydirectinput.keyUp('space')

def jump_forward():
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('space')
    time.sleep(10)
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('space')

def destroy():
    pydirectinput.click(button='left')
    
def place():
    pydirectinput.click(button='right')

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
    
    if "forward" in command:
        go_forward()
    elif "backward" in command:
        go_backward()
    elif "left" in command:
        go_left()
    elif "right" in command:
        go_right()  
    elif "slot one" in command:
        slot_1()
    elif "jump" in command:
        jump()
    elif "break" in command:
        destroy()
    elif "put" in command:
        place()
    elif "go up" in command:
        jump_forward()
    # Add more commands and associated functions as needed

except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")
except sr.RequestError:
    print("Sorry, I couldn't request results. Please check your internet connection.")