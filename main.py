import pyautogui
import speech_recognition as sr
import time


time.sleep(2)  # Pour que vous puissiez basculer vers votre jeu
recognizer = sr.Recognizer()


def go_forward():
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')


def go_backward():
    pyautogui.keyDown('s')
    time.sleep(2)
    pyautogui.keyUp('s')


def go_left():
    pyautogui.keyDown('a')
    time.sleep(2)
    pyautogui.keyUp('a')


def go_right():
    pyautogui.keyDown('d')
    time.sleep(2)
    pyautogui.keyUp('d')


def slot_1():
    pyautogui.keyDown('1')
    time.sleep(0.1)
    pyautogui.keyUp('1')


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')


def jump_forward():
    pyautogui.keyDown('w')
    pyautogui.keyDown('space')
    time.sleep(10)
    pyautogui.keyUp('w')
    pyautogui.keyUp('space')


def destroy():
    pyautogui.click(button='left')


def place():
    pyautogui.click(button='right')


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
    # Ajoutez d'autres commandes et fonctions associées au besoin

except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")
except sr.RequestError:
    print("Sorry, I couldn't request results. Please check your internet connection.")
