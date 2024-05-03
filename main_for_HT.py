import pyautogui
import speech_recognition as sr
import threading
from HeadTracking import headtracking as ht


def stop():
    for i in last_input:
        pyautogui.keyUp(i)
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
    pyautogui.keyDown('1')

def jump():
    pyautogui.keyDown('space')

def jump_forward():
    pyautogui.keyDown('w')
    pyautogui.keyDown('space')
    last_input.append('w')
    last_input.append('space')

def destroy():
    pyautogui.click(button='left')

def place():
    pyautogui.click(button='right')

def use_microphone(recognizer, source, timeout):
    print("Listening...")
    audio = recognizer.listen(source, timeout=timeout)
    return audio





last_input = []
recognizer = sr.Recognizer()


timeout_counter = 0
listening = False



def detect_head_movements():
    while True :
        if ht.head_center_x < ht.THRESHOLD:
            pyautogui.move(-10, 0)  # Déplacer la souris vers la gauche
        elif ht.head_center_x > 1 - ht.THRESHOLD:
            pyautogui.move(10, 0)  # Déplacer la souris vers la droite


        # Déplacer la souris si la tête dépasse le seuil
        if ht.head_center_y < ht.THRESHOLD:
            pyautogui.move(0, -10)  # Déplacer la souris vers le haut
        elif ht.head_center_y > 0.75 - ht.THRESHOLD:
            pyautogui.move(0, 10)  # Déplacer la souris vers le bas



def take_command():
    while True:
            with sr.Microphone() as source:
                print('listening...')
                voice = recognizer.listen(source)
                command = recognizer.recognize_google(voice)
                command = command.lower()
                if 'command' in command:
                    command = command.replace('command', '')
                    print(command)
        
                return command


def run_microphone():
    while True:
        command = take_command()
        print(command)
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
        elif "up" in command:
            jump_forward()
        elif "stop" in command:
            stop()
        else:
            print('Please say the command again.')


# Création des threads
mic_thread = threading.Thread(target=run_microphone)
head_movement_thread = threading.Thread(target=detect_head_movements)

# Démarrage des threads
mic_thread.start()
head_movement_thread.start()

# Attente de la fin des threads (ce blocage du programme permet de garder les threads actifs)
mic_thread.join()
head_movement_thread.join()