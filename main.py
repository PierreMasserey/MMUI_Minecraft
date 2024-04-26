import pyautogui
import speech_recognition as sr
import time


time.sleep(2)  # Pour que vous puissiez basculer vers votre jeu
recognizer = sr.Recognizer()

last_input = []
def stop(input):
    pyautogui.keyUp(input)
    last_input.clear()

def go_forward():
    pyautogui.keyDown('w')
    last_input.append('w')


def go_backward():
    pyautogui.keyDown('s')
    last_input.append('s')

def go_left():
    pyautogui.keyDown('a')
    last_input.append('a')


def go_right():
    pyautogui.keyDown('d')
    last_input.append('d')


def slot_1():
    pyautogui.press('1')

def jump():
    pyautogui.press('space')


def jump_forward():
    pyautogui.hotkey('w', 'space')
    last_input.append('w')
    last_input.append('space')


def destroy():
    pyautogui.click(button='left')


def place():
    pyautogui.click(button='right')


with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    #print(audio)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
    print(type(command))
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
    # Ajoutez d'autres commandes et fonctions associées au besoin

except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")
except sr.RequestError:
    print("Sorry, I couldn't request results. Please check your internet connection.")
